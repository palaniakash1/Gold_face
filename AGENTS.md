# Gold Face - Agent Coding Guidelines

## Project Overview

**Gold Face** is a virtual jewelry try-on application using computer vision. It has two implementations:
- **Desktop App**: Python/OpenCV with dlib face detection (`new_main.py`)
- **Web App**: Browser-based with MediaPipe Face Mesh (`webapp/index.html`)

## Running the Project

### Web App (Recommended)
```bash
cd webapp
python server.py
# Opens at http://localhost:8000
```

### Desktop App
```bash
# Requires: Python 3.12, opencv-python, numpy, dlib
python new_main.py

# Controls:
#   n - Next jewelry combination
#   ESC - Exit
```

### Project Launcher
```bash
python run_project.py
```

### MediaPipe Face Mesh (Web App)
The webapp uses **MediaPipe Face Mesh** for face detection with 468 landmarks:
- **Ear landmarks**: 234 (left), 454 (right) - actual ear outer points
- **Chin landmark**: 152
- **Nose tip**: 1

CDN URLs:
```
https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/face_mesh.js
https://cdn.jsdelivr.net/npm/@mediapipe/camera_utils/camera_utils.js
```

## Build/Test/Lint Commands

```bash
# Python linting (ruff)
ruff check .
ruff check new_main.py

# Format Python code
ruff format .

# Check Python syntax
python -m py_compile new_main.py

# Verify webapp HTML syntax
# (Open in browser and check console)
```

## Code Style Guidelines

### General Principles
- Write clear, readable code with descriptive variable names
- Handle errors gracefully with informative messages
- Test code manually when automated tests aren't available

---

## Python Style Guide

### Imports
```python
# Standard library imports first
import os
import sys
from math import hypot

# Third-party imports second
import cv2
import numpy as np
import dlib

# Local imports last
# (if applicable)

# Sort alphabetically within each group
```

### Formatting
- Line length: 88 characters (ruff default)
- Use 4 spaces for indentation
- Add trailing commas in multi-line structures
- Use parentheses for line continuations
```python
# Good
result = some_function(
    argument1,
    argument2,
    argument3,
)

# Bad
result = some_function(argument1, argument2, argument3)
```

### Naming Conventions
```python
# Variables: snake_case
necklace_images = []
current_index = 0
face_landmarks = []

# Constants: UPPER_SNAKE_CASE
MAX_FRAME_WIDTH = 640
THRESHOLD_VALUE = 25

# Functions: snake_case (verb phrase preferred)
def load_jewelry_images():
def detect_faces(frame):

# Classes: PascalCase (if applicable)
class FaceDetector:

# Files: snake_case.py
new_main.py, face_utils.py
```

### Error Handling
```python
# Always handle resource cleanup
cap = cv2.VideoCapture(0)
try:
    if not cap.isOpened():
        print("Error: Cannot open webcam. Please check connection.")
        exit()
finally:
    cap.release()
    cv2.destroyAllWindows()

# Check return values from functions
ret, frame = cap.read()
if not ret or frame is None:
    print("Error: Failed to capture frame")
    break
```

### Type Hints (Recommended for new code)
```python
from typing import List, Tuple, Optional

def process_frame(frame: np.ndarray) -> Tuple[np.ndarray, int]:
    """Process a video frame and return modified frame."""
    return processed_frame, face_count
```

---

## JavaScript/HTML Style Guide

### JavaScript
```javascript
// Use const for variables that don't change
const video = document.getElementById('video');
let currentIndex = 0;

// Prefer arrow functions
const processImage = (img) => {
    return processedCanvas;
};

// Use descriptive names
const currentNecklaceIndex = 0;
const isModelLoaded = false;

// Async/await for asynchronous operations
async function loadModels() {
    try {
        await faceapi.nets.tinyFaceDetector.loadFromUri(url);
    } catch (error) {
        console.error('Error loading models:', error);
    }
}

// Always handle errors
img.onerror = () => {
    console.error('Failed to load image');
};
```

### HTML
```html
<!-- Use semantic HTML elements -->
<header>, <main>, <section>, <footer>

<!-- Keep attributes in lowercase -->
<div class="container" data-value="test">

<!-- Use meaningful IDs -->
<video id="camera-feed">
```

### CSS
```css
/* Use CSS custom properties for colors */
:root {
    --primary-color: #ffd700;
    --bg-dark: #1a1a2e;
}

/* Group related properties */
.video-container {
    position: relative;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(255, 215, 0, 0.2);
}

/* BEM naming for complex components */
.gallery-category__title {}
.thumbnail--active {}
```

---

## Project Structure

```
Gold_face/
├── new_main.py           # Desktop app entry point
├── run_project.py        # Project launcher
├── run.bat               # Windows batch launcher
├── webapp/
│   ├── index.html        # Web app (main file)
│   ├── server.py         # HTTP server
│   └── jewelry/          # Jewelry images
│       ├── necklace/
│       └── earring/
├── earring/              # Desktop app jewelry
├── necklace/             # Desktop app jewelry
├── shape_predictor_68_face_landmarks.dat  # dlib model (95MB)
└── dlib-*.whl            # Pre-built dlib wheel
```

## Important Notes

### Dependencies
- **Python 3.12 required**
- **NumPy 1.26.4** - MUST use this version (NumPy 2.x incompatible with dlib 19.24.99)
- **dlib 19.24.99** - Pre-built wheel provided for Windows

### CORS Policy
- External image URLs must support CORS for the web app
- **Blocked**: Pinterest, Instagram, Facebook, Twitter URLs
- **Allowed**: imgur, imgbb, postimages, direct image links

### Git Large Files
- `shape_predictor_68_face_landmarks.dat` is 95MB (GitHub limit: 50MB)
- Use Git LFS for large files or keep in .gitignore

### Debugging
- Python: Check `cv2.imread()` return values before processing images
- JavaScript: Check `img.onload` and `img.onerror` for image loading
- Camera: Verify webcam permissions and availability
