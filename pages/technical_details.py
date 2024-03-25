import streamlit as st
def show():
    # st.title("Recurrent Neural Network")

    # Sidebar for navigation
    st.sidebar.title("Navigation")

    section = st.sidebar.radio("Go to", ["Introduction", "The Data", "The Model", "Future work"])

    st.markdown("""
            <style>
            .big-font {
                font-size:20px;
            }
            </style>
            """, unsafe_allow_html=True)

    # Conditional rendering of content based on sidebar navigation
    if section == "Introduction":
        st.header("Introduction")

        st.markdown("""
                    <div>

                    Recently, the music world was abuzz with the release of a new single from Drake, marked by the catchy lyrics and beats that fans have come to expect.
                    But the story took an unexpected turn when it was revealed that the mastermind behind this hit wasn't Drake at all—it was an artificial intelligence.
                    This revelation didn't just stir up the music industry; it sparked a profound fascination within me.

                    Thus began this passion project.</div>""", unsafe_allow_html=True)
        st.write("")

        st.image('content_images/drakeWeekend.webp')



    elif section == "The Data":
        st.header("The Data")
        st.markdown("""

        <div>
        For my dataset, I utilized the Cymatics EDM sample pack. My decision to work with an EDM dataset was driven by two main factors: firstly, my personal affinity for EDM music, and secondly, EDM's inherently repetitive nature, which I believed would facilitate the model's ability to discern patterns more easily.

        <br><br>
        <b>Data processing:<b>

        The dataset utilized for this music generation project is in the MIDI format, a standard file format used to encode musical information.
        To effectively process and analyze this dataset, I used Music21, a comprehensive Python library specifically designed for musicology.
        Music21 offers a wide array of tools and functionalities, enabling the parsing, examination, and manipulation of MIDI files.
        This library simplifies the task of extracting musical elements such as notes, chords, and even instruments from the dataset.

        </div>""", unsafe_allow_html=True)



    elif section == "The Model":
        st.header("The Model")
        st.write("""

        Recurrent Neural Networks (RNNs) are a type of artificial neural network optimized for pattern recognition in sequential data, like the melodies and rhythms found in music. By processing sequences of musical elements, RNNs retain internal memory, essential for understanding the temporal dynamics and dependencies in music compositions. This process, depicted below as a sequence of inputs labeled A, B, C, and D, allows RNNs to generate music that logically progresses over time, reflecting learned patterns from comprehensive music datasets.

        A unique variant of RNNs, Long Short-Term Memory (LSTM) networks, further refine this process. LSTMs are specifically designed to overcome the challenges of long-term musical dependencies that traditional RNNs struggle with, mainly due to the vanishing gradient problem. This issue makes it tough for standard RNNs to maintain the learning of correlations between musical events separated by significant time gaps within a piece.

        As shown in the diagram, LSTM networks enhance the basic RNN structure by incorporating memory cells that have gates to manage the flow of information. These gates are critical—they allow the network to retain or forget information, ensuring that significant musical motifs and themes are preserved across extended sequences. You can see this in the transition from inputs A, B, C, D to B, C, D, E, where the LSTM network selectively carries forward relevant information to inform the next sequence of music generation.


        """)

        st.image('content_images/rnn-diagram.png', width=250)


    elif section == "Future work":
        st.header("Transformer Model")
        st.write("""

        Using MIDI files and LSTM (Long Short-Term Memory) networks for music generation has its limitations. MIDI files, while compact and versatile, primarily encode musical notes and their attributes such as pitch, velocity, and duration, but lack the complexity of actual audio recordings. This simplification can result in music that misses the nuanced expressions and textures found in different genres. They also require substantial data preprocessing and can be computationally intensive for training on large datasets.

        Trying a Transformer models and WAV format audio files could offer significant benefits. Transformers, with their self-attention mechanisms, excel in capturing complex relationships in data, making them better suited for understanding the intricacies of musical composition and style. When paired with WAV files, which provide a direct representation of sound waves, the resulting system could capture the full spectrum of musical expression, including timbre, dynamics, and articulation that MIDI lacks.
        """)

        st.image('content_images/OPTransformer.jpeg')



if __name__ == "__main__":
    show()
