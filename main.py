# main.py

from toor_distance.image_processor import load_image
from UI.view import display_image

def main():

    img = load_image()

    print(img.shape)
    
    display_image(img)

if __name__ == "__main__":
    main()