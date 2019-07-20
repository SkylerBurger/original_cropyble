try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

from os.path import abspath

print('\n*************')
# print('FANGO:') 
# print(pytesseract.image_to_string('fango.jpg'))
# print('\n*************')
# print('SOCKS:')
# print(pytesseract.image_to_string(Image.open('socks.jpg')))
# print('\n*************')
# print('ORCHID:')
# print(pytesseract.image_to_string('orchid_care.jpg'))
# print('\n*************')

print(pytesseract.image_to_boxes(Image.open('socks.jpg')))