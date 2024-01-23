import os
import fire        
from PIL import Image

class ImageResizer:
    """
    A tool that resizes images while maintaining aspect ratio and adds a specified background color.

    Args:
        input_dir (str): The directory path where the input images are located.
        output_dir (str): The directory path where the resized images will be saved.
            If '' is specified for output_dir, the resized images will be saved to '_out' in the input directory.
        image_size (tuple): The size (width, height) of the resized images.
        background_color (tuple): The RGBA tuple (r,g,b,a) representing the background color of the resized images.
    """

    def __init__(self, input_dir, output_dir='', image_size=(1024,1024), background_color=(0,0,0,0)):
        self.input_dir = input_dir
        if output_dir == '':
            self.output_dir = os.path.join(input_dir, '_out')
        else:
            self.output_dir = output_dir
        self.image_size = image_size
        self.background_color = background_color

    def __call__(self):
        """
        Resizes the images in the input directory while maintaining aspect ratio and adds a specified background color.

        The resized images are saved to the output directory.

        Returns:
            None
        """
        # Make output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        # Get the list of image files in the input directory
        image_files = [file for file in os.listdir(self.input_dir) \
                       if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png')]
        # Sort the list of image files
        image_files.sort()
        # Iterate over each image file
        for file in image_files:
            # Open the image file
            image_path = os.path.join(self.input_dir, file)
            # Print the filename.
            print(image_path, end='')
            image = Image.open(image_path)
            # Resize the image while maintaining aspect ratio
            # Calculate the aspect ratio of the original image
            original_width, original_height = image.size
            aspect_ratio = original_width / original_height

            # Calculate the new width and height based on the aspect ratio
            if aspect_ratio < 1.0:
                new_height = self.image_size[1]
                new_width = int(new_height * aspect_ratio)
            else:
                new_width = self.image_size[0]
                new_height = int(new_width / aspect_ratio)

            # Resize the image while maintaining aspect ratio
            resized_image = image.resize((new_width, new_height), resample=Image.BICUBIC)
            # Create a new image with the specified background color
            new_image = Image.new('RGBA', self.image_size, self.background_color)
            # Paste the resized image onto the new image
            new_image.paste(resized_image, ((self.image_size[0] - new_width) // 2, (self.image_size[1] - new_height) // 2))
            # Convert the image to RGB mode
            new_image = new_image.convert('RGBA')
            # Save the new image to the output directory as JPEG
            output_path = os.path.join(self.output_dir, file.replace('.jpeg', '.png').replace('.jpg', '.png'))
            new_image.save(output_path, 'PNG')
            # Print the filename of the resized image.
            print(' ->', output_path)

if __name__ == '__main__':
    fire.Fire(ImageResizer)
