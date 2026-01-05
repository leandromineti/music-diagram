import matplotlib.pyplot as plt
import numpy as np

def get_chromatic_scale():
    return ['C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab', 'A', 'A#/Bb', 'B']

def create_chromatic_circle_image():
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
    # 0 degrees is East. We want C at Top (90 degrees).
    # Angle = 90 - (i * 30)
    
    for i, note in enumerate(notes):
        angle_deg = 90 - (i * 30)
        angle_rad = np.radians(angle_deg)
        
        # Calculate position
        x = np.cos(angle_rad)
        y = np.sin(angle_rad)
        
        # Add text
        # Adjust alignment based on position to avoid overlapping the circle line too much
        ha = 'center'
        va = 'center'
        
        # Add a background box for better readability
        ax.text(x, y, note, fontsize=16, fontweight='bold', ha=ha, va=va,
                bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

    output_file = 'chromatic_circle.png'
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Diagram saved to {output_file}")

if __name__ == "__main__":
    create_chromatic_circle_image()
