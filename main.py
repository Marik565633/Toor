# main.py

from pathlib import Path
from UI.view import display_image


def main():

    image_paths = sorted(
        Path("data").glob("*.jpg")
    )

    display_image(image_paths)


if __name__ == "__main__":
    main()