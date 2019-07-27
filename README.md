# Text to Crop

**Author**: Skyler Burger
**Version**: 2.0.0

## Overview
This project uses optical character recognition (OCR) to create a record of the text within an image and stores it in a Cropable object. Calls can then be made to the Cropable object to generate output images that are crops of the original image that contain the search query.

## Getting Started
- Clone this repo to your machine with `git clone https://github.com/SkylerBurger/text_to_crop.git`
- Install tesseract on your machine with `sudo apt-get install tesseract-ocr`
- Create a Python virtual environment from within the top-level directory of this repo with `pipenv shell`
- Install the required dependencies within your virtaul environment with `pipenv install`
- Put images you'd like to OCR into the /input_images directory
- Run main.py with `python main.py`

## Architecture
### Packages
- [**pillow**](https://python-pillow.org/)
- [**pytesseract**](https://github.com/madmaze/pytesseract)
- [**tesseract**](https://github.com/tesseract-ocr/tesseract)


## API
- **Cropable()**: Takes an input image location, performs OCR and stores the results for future crops.
- **.crop()**: Takes in a query string representing the word you'd like cropped from the image. Generates and saves a cropped copy of the original image based on the query string.


## Change Log
07/22/2019 - 1.1.0
- Corrected bounding box math. Images are being properly cropped.

07/27/2019 - 2.0.0
- Refactored cropping functions into a class to minimize work needed to perform multiple crops on a single image.
