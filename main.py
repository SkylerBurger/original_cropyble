from os.path import abspath
import re

from PIL import Image
import pytesseract


# 1. Get the text query
text_query = input('\nWhat text would you like to search for?: ')

# 2. Convert image to image string
input_image = input('\nWhich image would you like to search?: ')
image_string = pytesseract.image_to_string(Image.open(f'input_images/{input_image}'))

print(image_string)

# 3. Find text query matches in the image string
regex_object = re.compile(f'(^|\s)({text_query})(\s)', re.IGNORECASE)
match_object = regex_object.search(image_string)

if match_object:
    print(match_object.group(2))
else:
    print('Text query was not located in the input image.')
#     a. If match found, covert image to boxes
#     b. If no match found, return message
# 4. Find lines in image to boxes output that match the text query
# 5. Grab the top-left coordinates of first letter and bottom-right coordinates of the last letter
# 6. Use Image.crop() to create a new image based on those coordinates
# 7. Save the newly cropped image