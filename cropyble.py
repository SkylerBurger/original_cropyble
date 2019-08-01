import os

from PIL import Image
import pytesseract


class Cropyble:
    """Container for OCR and cropping methods."""
    def __init__(self, input_image):
        """Initializes a Cropyble object."""
        self.input_image_path = os.path.join(os.getcwd(), input_image)
        self.box_data = {}
        self.image_to_data()

    def image_to_data(self):
        """
        Utilizes pytesseract OCR to generate bounding box data for the image.
        Returns the bounding box data.
        """
        found_image = False
        while not found_image:
            try:
                print('Please wait.....')
                image_string = pytesseract.image_to_string(Image.open(self.input_image_path))
                word_box_data = pytesseract.image_to_data(Image.open(self.input_image_path))
                char_box_data = pytesseract.image_to_boxes(Image.open(self.input_image_path))
                found_image = True
            except FileNotFoundError:
                print(f'\nThe file [{self.input_image_path}] was not found.')
                self.input_image_path = input('Please enter the path for the image you\'d like to search: ')
        
        # TODO: Raise an error if no text is recognized
        print(f'\nRecognized Text:\n {image_string}')

        self.normalize_word_boxes(word_box_data)
        self.normalize_char_boxes(char_box_data)

    def normalize_word_boxes(self, word_box_data):
        word_box_data = word_box_data.split('\n')
        word_box_data = word_box_data[1:]

        lines = [line.split('\t') for line in word_box_data]
        for line in lines:
            self.box_data[line[11]] = [int(line[6]), int(line[7]), 
                (int(line[6]) + int(line[8])), (int(line[7]) + int(line[9]))]

    def normalize_char_boxes(self, char_box_data):
        # TODO: Verify one entry per letter in alphabetical order (it confused a D with an O)
        char_box_data = char_box_data.split('\n')
        
        lines = [line.split(' ') for line in char_box_data]
        for line in lines:
            self.box_data[line[0]] = [int(line[1]), int(line[2]), int(line[3]), int(line[4])]

    def crop(self, text_query, output_path):
        """
        Takes in a text query string.
        Outputs an image of the query from the input image if present.
        """
        original_image = Image.open(self.input_image_path)
        box = self.box_data[text_query]
        
        new_image = original_image.crop((box[0], box[1], box[2], box[3]))

        output_path = os.path.join(os.getcwd(), output_path)
        new_image.save(output_path)
        print(f'Finished!\nResults saved at: {output_path}\n')


if __name__ == "__main__":

    input_image = input('\nPlease enter the path for the image you\'d like to search: ')
    output_path = input('\nPlease enter the path for the output image: ')
    my_image = Cropyble(input_image)

    text_query = input('\nWhich word would you like to search for?: ')
    my_image.crop(text_query, output_path)
