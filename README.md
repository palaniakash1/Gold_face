# Gold Face - Virtual Jewelry Try-On

A real-time virtual jewelry try-on application using computer vision and face landmark detection.

## Features

- **Real-time Face Detection** - Uses MediaPipe Face Mesh (468 landmarks) for accurate face tracking
- **Virtual Jewelry Overlay** - Dynamically places necklaces and earrings on your face
- **Auto Background Removal** - Smart background removal for any jewelry image
- **Custom Jewelry Upload** - Add your own jewelry images (upload or paste URL)
- **Photo Capture** - Save your look with jewelry to your device
- **Responsive Design** - Works on desktop and mobile browsers
- **Mirror Mode** - Camera is mirrored for natural selfie experience
- **Gallery Collection** - Browse and select from multiple jewelry options

## Running the Project

### Web App (Recommended)

```bash
cd webapp
python server.py
```

Then open http://localhost:8001 in your browser.

**Requirements:**
- Python 3.x
- Modern browser (Chrome, Firefox, Safari, Edge)
- Webcam access

### Desktop App

```bash
# Install dependencies first
pip install -r requirements.txt

# Run from src directory
cd src
python main.py
```

**Controls:**
| Key | Action |
|-----|--------|
| `n` | Next jewelry combination |
| `ESC` | Exit |

### Using Launcher

```bash
python src/run_project.py
# or
run.bat
```

## Project Structure

```
gold_face/
├── README.md              # This file
├── AGENTS.md              # Agent coding guidelines
├── .gitignore            # Git ignore rules
├── requirements.txt       # Python dependencies
├── run.bat               # Windows launcher
│
├── src/                  # Desktop app (Python)
│   ├── main.py           # Main application
│   ├── run_project.py    # Project launcher
│   └── assets/           # Jewelry images
│       ├── earring/
│       │   ├── earring_1.jpg
│       │   ├── earring_2.jpg
│       │   └── earring_3.jpg
│       └── necklace/
│           ├── necklace_1.png
│           ├── necklace_2.png
│           └── necklace_3.png
│
├── webapp/               # Web application
│   ├── index.html        # Main webapp (MediaPipe Face Mesh)
│   ├── server.py         # HTTP server
│   ├── pictures/         # Captured photos (downloaded here)
│   └── jewelry/          # Webapp jewelry images
│       ├── earring/
│       └── necklace/
│
├── shape_predictor_68_face_landmarks.dat  # dlib model (95MB)
└── dlib-19.24.99-cp312-cp312-win_amd64.whl  # Pre-built dlib wheel
```

## Adding Custom Jewelry

### Web App
1. Click **"+ Add Custom"** button in the gallery
2. Choose **Upload** to select an image file, or **URL** to paste a direct image URL
3. Works with: imgur, imgbb, postimages

**Image Requirements:**
- **Necklaces**: PNG with transparent background (recommended)
- **Earrings**: Single image with left and right earrings side-by-side

### Supported URL Sources
| Service | Works? |
|---------|--------|
| imgur.com | ✅ |
| imgbb.com | ✅ |
| postimages.org | ✅ |
| Direct .png/.jpg links | ✅ |
| Pinterest | ❌ (CORS blocked) |
| Instagram | ❌ (CORS blocked) |
| Facebook | ❌ (CORS blocked) |
| Twitter | ❌ (CORS blocked) |

## Technology Stack

### Web App
- **MediaPipe Face Mesh** - 468 face landmarks
- **HTML5 Canvas** - Real-time overlay rendering
- **CSS3** - Premium mobile-first design
- **JavaScript** - Vanilla JS (no frameworks)

### Desktop App
- **Python 3.12**
- **OpenCV** - Computer vision
- **dlib** - Face landmark detection (68 points)
- **NumPy** - Numerical operations

## Face Landmarks

### Web App (MediaPipe Face Mesh - 468 points)
```
Left Ear:     Landmark 234
Right Ear:    Landmark 454
Chin:         Landmark 152
Nose Tip:     Landmark 1
```

### Desktop App (dlib - 68 points)
```
Left Ear:     Point 1
Right Ear:    Point 16
Chin:         Point 8
```

## Dependencies

### Python (Desktop App)
```bash
pip install -r requirements.txt
```

Required packages:
- Python 3.12
- NumPy 1.26.4 (NumPy 2.x incompatible with dlib 19.24.99)
- opencv-python
- dlib 19.24.99

### Browser (Web App)
- Modern browser with WebRTC support
- Camera permissions

## Known Limitations

1. **Earring Positioning** - May need adjustment based on face shape
2. **Background Removal** - Works best with solid white/black backgrounds
3. **Lighting** - Best results in good lighting conditions
4. **Face Coverage** - Requires clear view of face (no obstructions)

## License

MIT License

## Acknowledgments

- [MediaPipe](https://google.github.io/mediapipe/) - Face Mesh by Google
- [dlib](http://dlib.net/) - Machine learning toolkit
