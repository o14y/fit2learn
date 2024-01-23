# fit2learn

NAME
    fit2learn.py - A tool that resizes images while maintaining aspect ratio and adds a specified background color.

SYNOPSIS
    fit2learn.py --input_dir=INPUT_DIR <flags>

DESCRIPTION
    A tool that resizes images while maintaining aspect ratio and adds a specified background color.

ARGUMENTS
    INPUT_DIR
        The directory path where the input images are located.

FLAGS
    -o, --output_dir=OUTPUT_DIR
        Default: ''
        The directory path where the resized images will be saved. If '' is specified for output_dir, the resized images will be saved to '_out' in the input directory.
    -i, --image_size=IMAGE_SIZE
        Default: (1024, 1024)
        The size (width, height) of the resized images.
    -b, --background_color=BACKGROUND_COLOR
        Default: (0, 0, 0, 0)
        The RGBA tuple (r,g,b,a) representing the background color of the resized images.