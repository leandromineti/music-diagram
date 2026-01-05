# Chromatic Note Diagram Generator

This project contains a simple Python script that generates a visual representation of the chromatic scale in a circular diagram. It includes enharmonic equivalents (e.g., C#/Db).

## Description

The script uses `matplotlib` to create a high-quality PNG image of the 12 notes of the chromatic scale arranged in a circle, similar to a clock face, with C at the top.

## Prerequisites

- Python 3.x
- `matplotlib`
- `numpy`

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/leandromineti/music-diagram.git
    cd music-diagram
    ```

2.  Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    ```

3.  Install the required packages:
    ```bash
    pip install matplotlib numpy
    ```

## Usage

Run the script using Python:

```bash
python chromatic_diagram.py
```

This will generate a file named `chromatic_circle.png` in the current directory.

## Output Example

The script generates an image like this:

![Chromatic Circle](chromatic_circle.png)
