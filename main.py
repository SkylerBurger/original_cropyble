from text_to_crop import image_query


# 1. Get the text query
text_query = input('\nWhat text would you like to search for?: ')
input_image = input('\nWhich image would you like to search?: ')
image_query(text_query, input_image)


# 4. Find lines in image to boxes output that match the text query
# 5. Grab the top-left coordinates of first letter and bottom-right coordinates of the last letter
# 6. Use Image.crop() to create a new image based on those coordinates
# https://pillow.readthedocs.io/en/stable/reference/Image.html
# 7. Save the newly cropped image