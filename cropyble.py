from PIL import Image
import pytesseract


class Cropyble:
    """Container for OCR and cropping methods."""
    def __init__(self, input_image):
        self.input_image = input_image
        self.box_data = self.image_to_data()

    def image_to_data(self):
        """
        Utilizes pytesseract OCR to generate bounding box data for the image.
        Returns the bounding box data.
        """
        # TODO: Generalize this so input image can be located anywhere
        found_image = False
        while not found_image:
            try:
                print('Please wait.....')
                image_string = pytesseract.image_to_string(Image.open(f'input_images/{self.input_image}'))
                box_data = pytesseract.image_to_data(Image.open(f'input_images/{self.input_image}'))
                found_image = True
            except FileNotFoundError:
                print(f'\nThe file [{self.input_image}] was not found.')
                self.input_image = input('Which image would you like to search?: ')

        box_data = box_data.split('\n')
        box_data = box_data[1:]

        # TODO: Raise an error if no text is recognized
        print(f'\nRecognized Text:\n {image_string}')
        return box_data

    def crop(self, text_query):
        """
        Takes in a text query string.
        Outputs an image of the query from the input image if present.
        """
        word_box = self._find_word_box(text_query)
        self._crop_image(word_box)

    def _find_word_box(self, text_query):
        """
        Takes in a search query.
        Checks box data to see if the query is present in the image.
        Returns the bounding box coordinates for the query if present.
        """
        # TODO: Figure out best way to properly respond if query is not located.
        lines = [line.split('\t') for line in self.box_data]
        word_box = []
        for line in lines:
            if line[11] == text_query:
                print(f'\nI found: {text_query}')
                word_box.append(line)
                break
        if len(word_box) == 0:
            return
        word_box = [int(word_box[0][6]), 
                    int(word_box[0][7]), 
                    (int(word_box[0][6]) + int(word_box[0][8])), 
                    (int(word_box[0][7]) + int(word_box[0][9]))]
        return word_box

    def _crop_image(self, coordinates):
        """
        Takes in bounding box coordinates for a word in the image.
        Generates a cropped copy of the original image and saves it.
        """
        original_image = Image.open(f'input_images/{self.input_image}')
        
        new_image = original_image.crop((coordinates[0], 
                                        coordinates[1], 
                                        coordinates[2],
                                        coordinates[3]))
        # TODO: Allow user to specify the output file name and location
        new_image.save('output.jpg')
        print('Results saved as output.jpg')


if __name__ == "__main__":

    input_image = input('\nWhich image would you like to search?: ')
    my_image = Cropyble(input_image)

    text_query = input('\nWhat text would you like to search for?: ')
    my_image.crop(text_query)
