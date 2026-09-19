import cv2

from toor_distance.image_processor import load_image
from UI.keyboard import handle_key
from UI.mouse import mouse_callback


cv2.setMouseCallback("Image", mouse_callback)


def display_image(image_paths):

    current_frame = 0
    scale = 0.4
    current_tool = "circle"
    cv2.setMouseCallback("Image", mouse_callback)

    while True:

        # Load current image
        image = load_image(
            image_paths[current_frame].name
        )

        image_bgr = cv2.cvtColor(
            image,
            cv2.COLOR_RGB2BGR
        )

        h, w = image_bgr.shape[:2]

        new_w = int(w * scale)
        new_h = int(h * scale)

        display = cv2.resize(
            image_bgr,
            (new_w, new_h),
            interpolation=cv2.INTER_AREA
        )
    
        cv2.imshow("Image", display)

        key = cv2.waitKeyEx(20)

        if key != -1:

            print("Key =", key)

            result = handle_key(
                key,
                current_frame,
                len(image_paths), 
                current_tool
            )

            if result is None:
                break

            current_frame = result[0]
            current_tool = result[1]
            print("Current frame:", current_frame)
            print("Current tool:", current_tool)

    cv2.destroyAllWindows()