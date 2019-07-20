import re

from PIL import Image
import pytesseract


def image_query(text_query, image_location):
    # 2. Convert image to image string
    image_string = image_to_string(image_location)
    image_boxes = locate_text_matches(text_query, image_location, image_string)
    if image_boxes:
        # TODO: Determine the xy coords of the box containing the query string.
        
    else:
        return

def image_to_string(input_image):
    """
    Takes in a string representing an image's name.
    Utilizes pytesseract OCR to generate a string from the image.
    Returns the image string.
    """
    found = False
    while not found:
        try:
            image_string = pytesseract.image_to_string(Image.open(f'input_images/{input_image}'))
            found = True
        except FileNotFoundError:
            print(f'\nThe file {input_image} was not found.')
            input_image = input('Which image would you like to search?: ')

    print(f'\nI recognized:\n {image_string}')
    return image_string

def locate_text_matches(text_query, image_location, image_string):
    """
    Takes in a string representing the text query.
    Takes in a string representing the image's location
    Takes in a string representing character recognized in the image.
    Searches the image string for the contents of the text query.
    Returns a string of box locations of matched characters or None if there are not matches. 
    """
    regex_object = re.compile(f'(^|\s)({text_query})(\s)', re.IGNORECASE)
    match_object = regex_object.search(image_string)

    if match_object:
        # a. If match found, covert image to boxes
        print('\nI found: ', match_object.group(2))
        return pytesseract.image_to_boxes(Image.open(f'input_images/{image_location}'))
    else:
        # b. If no match found, return message
        print('Text query was not located in the input image.')
        return None

