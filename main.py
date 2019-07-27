from text_to_crop import Cropable


input_image = input('\nWhich image would you like to search?: ')
my_image = Cropable(input_image)

text_query = input('\nWhat text would you like to search for?: ')
my_image.crop(text_query)