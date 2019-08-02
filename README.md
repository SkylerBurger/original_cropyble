# Cropyble

**Author**: Skyler Burger
**Version**: 1.1.0

## Overview
Cropyble is a module that allows a user to easily perform crops on an image containing recognizable text. This module utilizes optical character recognition (OCR) from Google by way of pytesseract.

## Getting Started
### Linux & Mac OS
- Clone this repo to your machine with `git clone https://github.com/SkylerBurger/cropyble.git`
- Install tesseract on your machine with `sudo apt-get install tesseract-ocr`
- Create a Python virtual environment from within the top-level directory of this repo with `pipenv shell`
- Install the required dependencies within your virtaul environment with `pipenv install`
- Run main.py with `cropyble.py`

## Architecture
### Packages
- [**pillow**](https://python-pillow.org/)
- [**pytesseract**](https://github.com/madmaze/pytesseract)
- [**tesseract**](https://github.com/tesseract-ocr/tesseract)

### Python Standard Library
- [**os**](https://docs.python.org/3/library/os.html)

## API
- **Cropyble()**: Takes in a string representing the input image location. Cropyble runs OCR on the image and stores the bounding boxes for recognized words and characters for future crops.
- **.crop()**: Takes in a string representing the word or character you'd like cropped from the image and a second string representing the output image path. Generates a cropped copy of the query text from the original image and saves it at the specified location.

## Change Log
07/22/2019 - 0.1.0
- Corrected bounding box math. Images are being properly cropped.

07/27/2019 - 0.2.0
- Refactored cropping functions into a class to minimize work needed to perform multiple crops on a single image.

07/30/2019 - 0.3.0
- Cropyble can now accept a path for the input image and crop() accepts a path for the output image.

08/02/2019 - 1.1.0
- Cropyble can now crop words and characters recognized within an image using the same crop() method.
