import streamlit as st
st.set_page_config(
    page_title='Aria.ai',
    page_icon= "🎧"
)

import sys
import os


if 'streamlit' in os.environ:
    current_dir = os.getcwd()
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)


if os.path.exists('temp_Rocchetta.sf2'):
    os.remove('temp_Rocchetta.sf2')

if os.path.exists('temp_ClubSawHD.sf2'):
    os.remove('temp_ClubSawHD.sf2')

# Importing after adding the parent directory to the path
from predict import generate
import matplotlib.pyplot as plt
from mido import MidiFile
from music21 import instrument
import pretty_midi
import io
import numpy as np
import tempfile
from midi2audio import FluidSynth
import librosa
import librosa.display
from plots import plot_midi_notes_with_labels, plot_waveform


def generate_colored_text(text, colors):
    return "".join(
        f"<span style='color: {colors[i % len(colors)]}; font-size: 75px; font-weight: bold;'>{char}</span>"
        for i, char in enumerate(text)
    )

def align_text(text, alignment='left'):
    return f"<div style='text-align: {alignment};'>{text}</div>"

def add_bg_from_url(img, position='center'):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url({img});
            background-size: auto;
            background-position: {position};
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True)

import requests

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename



def show():
    rainbow_colors = ['#693C72', '#C15050', '#D97642', '#337357', '#D49D42']
    title = "Aria.ai 🎹"
    notes = "♩♫♪"
    colored_title = generate_colored_text(title, rainbow_colors)
    st.markdown(align_text(colored_title, 'left'), unsafe_allow_html=True)
    st.write('A lean learning Machine')

    img = """
    https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDlodmtyM3VjczRkNnNpemFhZ3ZsMXl0Mjg3ZXJhZHF6OHI1ODczbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/D3vTKclRSaLxT7YlUT/giphy.gif
    """
    add_bg_from_url(img)
    col1, col2 = st.columns(2)
    with col1:
        lead_instrument_option = st.selectbox(
            "Select lead instrument:",
            ['Piano', 'Guitar'],
            index=0,
            key='lead_instrument_selectbox'
        )

    with col2:
        st.write("Add accompanying instrument:")
        drums = st.checkbox("Drums", key="drums")
        # banjo = st.checkbox("Banjo", key="banjo")

    if 'lead_instrument' not in st.session_state:
        st.session_state['lead_instrument'] = None
    if 'additional_instruments' not in st.session_state:
        st.session_state['additional_instruments'] = []

    st.session_state['lead_instrument'] = instrument.Piano() if lead_instrument_option == 'Piano' else instrument.AcousticGuitar()
    st.session_state['additional_instruments'] = []
    if drums:
        st.session_state['additional_instruments'].append('Drums')
    # if banjo:
    #     st.session_state['additional_instruments'].append('Banjo')

    # Generating music...
    import time
    if st.button('Generate Music'):
        placeholder = st.empty()
        placeholder.text("Generating Music...")
        for i in range(40):
            placeholder.text(f"Generating Music{'.' * (i % 4 + 1)}")
            time.sleep(0.5)
        add_parts = st.session_state['additional_instruments']

        col1, col2, col3 = st.columns([1, 2, 4])
        with col3:
            fun_fact = st.empty()
            fun_fact.success("""

            Named 'Aria' in honor of the captivating solos that highlight operas and the boldness of Arya Stark,
            this title reflects the harmony between artistic elegance and the intelligent complexities of the Neural Network
                             """)

        generate(
            lead_instrument=st.session_state['lead_instrument'],
            add_parts=add_parts
        )

        placeholder.text("Music generation complete!")
        fun_fact.empty()

        add_bg_from_url(img, position='top right')
        midi_file = os.path.join('music_output', 'output.mid')
        st.title("Visual Midi Output")
        plot_midi_notes_with_labels(midi_file)


        soundfont_path_1 = 'https://storage.googleapis.com/aria-ai-bucket/Rocchetta.sf2'
        soundfont_path_2 = 'https://storage.googleapis.com/aria-ai-bucket/ClubSawHD.sf2'

        # local_soundfont_path_1 = download_file(soundfont_path_1, 'temp_Rocchetta.sf2')
        local_soundfont_path_2 = download_file(soundfont_path_2, 'temp_ClubSawHD.sf2')

        # Convert Original MIDI to WAV
        fs = FluidSynth(soundfont_path_1)
        fs.midi_to_audio(midi_file, 'music_output/output.wav')
        st.title("Original output")
        audio_path = 'music_output/output.wav'

        plot_waveform(audio_path)
        st.audio(audio_path)
        st.image('graph_images/wave.png')

        # Convert Original MIDI to EDM WAV

        fs = FluidSynth(local_soundfont_path_2)
        fs.midi_to_audio(midi_file, 'music_output/output_techno.wav')
        edm_track = 'music_output/output_techno.wav'
        st.title("EDM-ify")
        # st.write("""
        #         Note:

        #         The audio quality and overall harmony may vary based on the accompanying instruments chosen. (Just 'lead instuments' give better results)
        #         This can be attributed to the synth soundfont (.s2f) utilized (best I could find). See Technical details section.
        #         But, the idea is that you can import the file import a digital audio workstation like GarageBand
        #         and experiment with whichever sound you like.
        #          """)

        st.write("""

                same output, but passed through a synth soundfound

                 """)
        st.audio(edm_track)


        garageband_edited = 'https://storage.googleapis.com/aria-ai-bucket/track2.mp3'

        st.write("""

                    You can download the MIDI file and use it with software like GarageBand to create even more interesting sounds.
                    Here i'm using 'Sunrise Chord' from GarageBand.

                 """)
        st.audio(garageband_edited)

        col1, col2, col3, col4, col5 = st.columns([1,1,2,1,1])
        with open(midi_file, "rb") as file:
            with col3:
                st.download_button(
                    label="Download MIDI",
                    data=file,
                    file_name="generated_song.mid",
                    mime="audio/midi"
                )



footer="""<style>
.a {
    position: fixed;
    left: 0;
    bottom: 10px;
    width: 100%;
    background-color: white;
    color: black;
    text-align: center;
}
</style>
<div class="a">Made with ❤️ by Christelle </div>
"""
st.markdown(footer,unsafe_allow_html=True)


if __name__ == "__main__":
    show()
