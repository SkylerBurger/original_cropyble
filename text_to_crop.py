import re

from PIL import Image
import pytesseract


def image_query(text_query, image_location):
    # 2. Convert image to image string
    word_box = image_to_data(image_location, text_query.lower())
    if word_box:
        # TODO: Determine the xy coords of the box containing the query string.
        crop_image(word_box, image_location)
    else:
        print(f'Sorry, was not able to find {text_query} in image.')
        return

def image_to_data(input_image, text_query):
    """
    Takes in a string representing an image's name.
    Utilizes pytesseract OCR to generate bounding box data for the image.
    Returns the bounding box data.
    """
    found_image = False
    while not found_image:
        try:
            image_string = pytesseract.image_to_string(Image.open(f'input_images/{input_image}'))
            box_data = pytesseract.image_to_data(Image.open(f'input_images/{input_image}'))
            found_image = True
        except FileNotFoundError:
            print(f'\nThe file [{input_image}] was not found.')
            input_image = input('Which image would you like to search?: ')

    word_box = find_word_box(box_data, text_query)

    print(f'\nRecognized Text:\n {image_string}')
    return word_box


def find_word_box(box_data, text_query):
    box_data = box_data.split('\n')
    box_data = box_data[1:]
    lines = [line.split('\t') for line in box_data]
    word_box = []
    for line in lines:
        if line[11] == text_query:
            print(f'\nI found: {text_query}')
            word_box.append(line)
    if len(word_box) == 0:
        return
    word_box = [int(word_box[0][6]), 
                int(word_box[0][7]), 
                (int(word_box[0][6]) + int(word_box[0][8])), 
                (int(word_box[0][7]) + int(word_box[0][9]))]
    return word_box


def crop_image(coordinates, image_location):
    original_image = Image.open(f'input_images/{image_location}')
    
    new_image = original_image.crop((coordinates[0], 
                                    coordinates[1], 
                                    coordinates[2],
                                    coordinates[3]))
    new_image.save('output.jpg')
    Image.open('output.jpg')