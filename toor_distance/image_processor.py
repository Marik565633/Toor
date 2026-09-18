'''
Image processing module for specific dicom extracted images.
'''
import pathlib
from PIL import Image

DATA_DIR = pathlib.Path(__file__).resolve().parent.parent / 'data'


def load_image(filename='img-00000-00008.jpg', data_dir=DATA_DIR):
    '''Load an image from a file, by default from data directory.'''

    file_path = data_dir / filename
    img = Image.open(file_path)

    return img.numpy()
