import re

from PIL import Image
import pytesseract


def image_query(text_query, image_location):
    # 2. Convert image to image string
    image_string = image_to_string(image_location)
    image_boxes = locate_text_match(text_query, image_location, image_string)
    if image_boxes:
        # TODO: Determine the xy coords of the box containing the query string.
        crop_box = determine_crop_box(text_query, image_boxes)
        crop_image(crop_box, image_location)
    else:
        print('Sorry not found.')
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
            print(f'\nThe file [{input_image}] was not found.')
            input_image = input('Which image would you like to search?: ')

    print(f'\nRecognized Text:\n {image_string}')
    return image_string

def locate_text_match(text_query, image_location, image_string):
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
        print('\nMatched: ', match_object.group(2))
        return pytesseract.image_to_boxes(Image.open(f'input_images/{image_location}'))
    else:
        # b. If no match found, return message
        print('Search query was not located in the image.')
        return None

def determine_crop_box(text_query, text_boxes):
    text_boxes = text_boxes.split('\n')
    char_boxes = []
    counter = 0

    # Pull out the box lines related to the text query
    for line in text_boxes:
        if counter > len(text_query) - 1:
            break
        
        if line[0] == text_query[counter]:
            char_boxes.append(line)
            counter += 1
        elif line[0] == text_query[0]:
            char_boxes = [line]
            counter = 1
        else:
            char_boxes = []
            counter = 0

    char_boxes = [char_boxes[0], char_boxes[-1]]
    coordinates = {}
    regex_object = re.compile(r'.\s(\d*)\s(\d*)\s(\d*)\s(\d*)')
    match_object = regex_object.search(char_boxes[0])
    coordinates['x_top_left'] = match_object.group(1)
    coordinates['y_top_left'] = match_object.group(2)
    match_object = regex_object.search(char_boxes[1])
    coordinates['x_bottom_right'] = match_object.group(3)
    coordinates['y_bottom_right'] = match_object.group(4)

    return coordinates

def crop_image(coordinates, image_location):
    original_image = Image.open(f'input_images/{image_location}')
    
    xtl = int(coordinates['x_top_left'])
    ytl = int(coordinates['y_top_left'])
    xbr = int(coordinates['x_bottom_right'])
    ybr = int(coordinates['y_bottom_right'])
    
    
    new_image = original_image.crop((xtl, ytl, xbr, ybr))
    new_image.save('output.jpg')
    Image.open('output.jpg')