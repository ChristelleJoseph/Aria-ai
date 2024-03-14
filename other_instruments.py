
from music21 import tempo, instrument, note, chord, stream, percussion, duration

def create_hard_drum_track(measures, tempo=120):
    drum_part = stream.Part()
    drum_part.append(instrument.SnareDrum())  # Set the part as a percussion instrument

    # Define the drum pattern for each measure
    for measure in range(measures):
        for beat in range(4):  # Assuming a 4/4 time signature
            # Add a bass drum on beats 1 and 3
            if beat in [0, 2]:
                bass_drum = note.Note()
                bass_drum.pitch.midi = 36  # MIDI note for Acoustic Bass Drum
                bass_drum.duration = duration.Duration(1)  # One beat long
                drum_part.insert(measure * 4 + beat, bass_drum)

            # Add a snare drum on beats 2 and 4
            if beat in [1, 3]:
                snare_drum = note.Note()
                snare_drum.pitch.midi = 38  # MIDI note for Acoustic Snare
                snare_drum.duration = duration.Duration(1)
                drum_part.insert(measure * 4 + beat, snare_drum)

    return drum_part

# def create_Banjo_track(measures=16):
#     # Create a Stream for the banjo part
#     banjo_part = stream.Part()
#     banjo_part.insert(0, instrument.Banjo())

#     # melody_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
#     melody_notes = ['C', 'D', 'E', 'E', 'D', 'C']

#     # Iterate over the measures
#     for i in range(measures):
#         # Pick a note from the melody, cycling through the notes in the scale
#         note_name = melody_notes[i % len(melody_notes)]  # Cycle through notes within the scale
#         # Create a note
#         n = note.Note(note_name)
#         n.duration = duration.Duration("whole")  # One note per measure
#         banjo_part.append(n)

#     return banjo_part

# def create_Banjo_track(measures=16):
#     # Create a Stream for the banjo part
#     banjo_part = stream.Part()
#     banjo_part.insert(0, instrument.Banjo())

#     chord_progressions = [
#         ['G', 'B', 'D'],  # G Major
#         ['C', 'E', 'G'],  # C Major
#         ['D', 'F#', 'A', 'C'],  # D7
#         ['E', 'G', 'B'],  # E minor
#         ['A', 'C', 'E']  # A minor
#     ]

#     for i in range(measures):
#         chord_notes = chord_progressions[i % len(chord_progressions)]
#         current_chord = chord.Chord(chord_notes)
#         current_chord.duration = duration.Duration("whole")  # Set duration to whole note

#         banjo_part.append(current_chord)

#     return banjo_part


def create_Banjo_track(measures=16, scale_pattern=['C', 'D', 'E', 'G', 'A']):
    # Create a Stream for the banjo part
    banjo_part = stream.Part()
    banjo_part.insert(0, instrument.Banjo())

    # Define a basic melody pattern using a scale
    # This pattern can be adjusted to fit the style of the song better
    melody_notes = scale_pattern * (measures // len(scale_pattern) + 1)

    # Iterate over the measures
    for i in range(measures):
        # Pick a note from the melody pattern
        note_name = melody_notes[i % len(melody_notes)]  # Cycle through notes within the scale

        # Append the note four times per measure to create a melodic line
        for _ in range(4):
            n = note.Note(note_name)
            n.duration = duration.Duration("quarter")  # Set note duration to quarter for a melodic rhythm
            banjo_part.append(n)

    # Return the banjo part stream
    return banjo_part
