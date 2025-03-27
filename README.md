# PhotoQT - Simple Image Editor

## Description
PhotoQT is a lightweight image editor built with PyQt5 and PIL (Python Imaging Library). It allows basic image manipulation like rotation, filters, and adjustments.

![images/demo.png]

## Features
- Browse and select images from folders
- Apply various image transformations:
  - Rotate left/right
  - Mirror/flip
  - Convert to black & white
  - Adjust sharpness, color saturation, and contrast
  - Apply blur effect
- Simple, clean interface with dark theme
- Preserve original images while saving edits separately

## Requirements
- Python 3.x
- PyQt5
- Pillow (PIL fork)

## Installation
1. Install required packages:
   ```
   pip install PyQt5 Pillow
   ```

## Usage
1. Run the application:
   ```
   python photoqt.py
   ```
2. Click "Folder" to select a directory containing images
3. Select an image from the list
4. Use buttons or dropdown menu to apply transformations:
   - Left/Right: Rotate image
   - Mirror: Flip image horizontally
   - B/W: Convert to grayscale
   - Sharpen/Blur: Adjust image clarity
   - Color: Enhance saturation
   - Contrast: Adjust contrast

## Notes
- Edited images are automatically saved in an "Edits/" subfolder
- Original images remain unchanged
- Supported formats: JPG, JPEG, PNG, SVG

## License
Free to use and modify
