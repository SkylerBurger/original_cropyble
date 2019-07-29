# Cropyble

**Author**: Skyler Burger
**Version**: 2.0.0

## Overview
Cropyble is a module that allows a user to create a cropped image by simply searching an image for text. This module utilizes optical character recognition (OCR) from Google by way of pytesseract. Currently, input images will need to be of printed text for Cropyble to work properly.

## Getting Started
### Linux
- Clone this repo to your machine with `git clone https://github.com/SkylerBurger/cropyble.git`
- Install tesseract on your machine with `sudo apt-get install tesseract-ocr`
- Create a Python virtual environment from within the top-level directory of this repo with `pipenv shell`
- Install the required dependencies within your virtaul environment with `pipenv install`
- Copy images you'd like to OCR into the /input_images directory
- Run main.py with `cropyble.py`

## Architecture
### Packages
- [**pillow**](https://python-pillow.org/)
- [**pytesseract**](https://github.com/madmaze/pytesseract)
- [**tesseract**](https://github.com/tesseract-ocr/tesseract)


## API
- **Cropyble()**: Takes an input image location, performs OCR and stores the results for future crops.
- **.crop()**: Takes in a query string representing the word you'd like cropped from the image. Generates and saves a cropped copy of the original image based on the query string.


## Roadmap
- Installation instructions for other systems
- Integration with a handwriting recognition package
- Multiple match results
- Match highlighting applied to original image
- Proper Python packaging structure 

## Change Log
07/22/2019 - 1.1.0
- Corrected bounding box math. Images are being properly cropped.

07/27/2019 - 2.0.0
- Refactored cropping functions into a class to minimize work needed to perform multiple crops on a single image.
