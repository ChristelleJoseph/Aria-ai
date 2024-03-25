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

                    "Recently, the music world was abuzz with the release of a new single from Drake, marked by the catchy lyrics and beats that fans have come to expect.
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

                 Recurrent Neural Networks (RNNs) are a class of artificial neural networks that is well suited for music generation, as they excel in recognizing and generating patterns in sequential data, such as musical notes and rhythms. RNNs incorporate internal memory to process sequences of musical elements, enabling them to capture the temporal dynamics and dependencies of music. This capability allows RNNs to produce music that flows logically over time, capturing the essence of musical composition through learned patterns from extensive datasets of music.

                Long Short-Term Memory (LSTM) networks, a variant of RNNs, are particularly useful for music generation. They solve the critical challenge of learning and retaining long-term musical dependencies, an area where traditional RNNs falter due to the vanishing gradient problem. This problem makes it difficult for RNNs to learn correlations between musical events that are distant from each other in a piece. LSTMs address this by incorporating memory cells equipped with gates that regulate information flow, thus preserving important musical motifs and themes over longer sequences.

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
