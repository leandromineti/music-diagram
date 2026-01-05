import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def get_chromatic_scale():
    return ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

def get_chord_notes(root_note, chord_type):
    scale = get_chromatic_scale()
    root_idx = scale.index(root_note)
    
    intervals = {
        'Major': [0, 4, 7],
        'Minor': [0, 3, 7],
        'Diminished': [0, 3, 6],
        'Augmented': [0, 4, 8],
        'Major 7': [0, 4, 7, 11],
        'Minor 7': [0, 3, 7, 10],
        'Dominant 7': [0, 4, 7, 10]
    }
    
    if chord_type not in intervals:
        return []
        
    chord_indices = [(root_idx + interval) % 12 for interval in intervals[chord_type]]
    return [scale[i] for i in chord_indices]

def get_chord_intervals(chord_type):
    interval_names = {
        'Major': ['Root', 'Major 3rd', 'Perfect 5th'],
        'Minor': ['Root', 'Minor 3rd', 'Perfect 5th'],
        'Diminished': ['Root', 'Minor 3rd', 'Diminished 5th'],
        'Augmented': ['Root', 'Major 3rd', 'Augmented 5th'],
        'Major 7': ['Root', 'Major 3rd', 'Perfect 5th', 'Major 7th'],
        'Minor 7': ['Root', 'Minor 3rd', 'Perfect 5th', 'Minor 7th'],
        'Dominant 7': ['Root', 'Major 3rd', 'Perfect 5th', 'Minor 7th']
    }
    return interval_names.get(chord_type, [])

def draw_chromatic_circle(highlight_notes=None):
    if highlight_notes is None:
        highlight_notes = []
        
    notes = get_chromatic_scale()
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # Set limits and aspect
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    
    # Remove axes
    ax.axis('off')
    
    # Draw a circle
    circle = plt.Circle((0, 0), 1, color='lightgray', fill=False, linestyle='--')
    ax.add_artist(circle)
    
    # Place notes
    for i, note in enumerate(notes):
        angle_deg = 90 - (i * 30)
        angle_rad = np.radians(angle_deg)
        
        # Calculate position
        x = np.cos(angle_rad)
        y = np.sin(angle_rad)
        
        # Determine style based on whether note is in chord
        if note in highlight_notes:
            color = 'red'
            fontweight = 'bold'
            bbox_props = dict(facecolor='yellow', edgecolor='red', alpha=0.8, boxstyle='round,pad=0.5')
            fontsize = 18
        else:
            color = 'black'
            fontweight = 'normal'
            bbox_props = dict(facecolor='white', edgecolor='none', alpha=0.8)
            fontsize = 14
            
        # Add text
        ax.text(x, y, note, fontsize=fontsize, fontweight=fontweight, ha='center', va='center',
                bbox=bbox_props, color=color)

    return fig

def main():
    st.title('Chromatic Chord Visualizer')
    
    st.sidebar.header('Chord Builder')
    
    scale = get_chromatic_scale()
    root_note = st.sidebar.selectbox('Select Root Note', scale)
    
    chord_types = ['Major', 'Minor', 'Diminished', 'Augmented', 'Major 7', 'Minor 7', 'Dominant 7']
    chord_type = st.sidebar.selectbox('Select Chord Type', chord_types)
    
    chord_notes = get_chord_notes(root_note, chord_type)
    chord_intervals = get_chord_intervals(chord_type)
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.write(f"### {root_note} {chord_type}")
        fig = draw_chromatic_circle(chord_notes)
        st.pyplot(fig)
        
    with col2:
        st.write("### Chord Details")
        st.write("") # Add some spacing
        for note, interval in zip(chord_notes, chord_intervals):
            st.markdown(f"**{interval}**: {note}")

if __name__ == "__main__":
    main()
