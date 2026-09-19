import cv2

from toor_distance.image_processor import load_image
from UI.keyboard import handle_key
from UI.mouse import mouse_callback
from UI.draw import draw_tool


def display_image(image_paths):

    current_frame = 0
    scale = 0.4
    current_tool = "circle"

    circles = [
        {
            "x": 100,
            "y": 200,
            "radius": 20
        }
    ]

    lines = []

    state = {
        "circles": circles,
        "lines": lines,
        "tool": current_tool,

        "selected_circle": None,
        "dragging": False,

        "selected_line": None,
        "dragging_line": False
    }

    cv2.namedWindow("Image")

    cv2.setMouseCallback(
        "Image",
        mouse_callback,
        state
    )

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

        # Draw circles
        for circle in circles:

            color = (0, 255, 0)

            if state["selected_circle"] is circle:
                color = (0, 0, 255)

            cv2.circle(
                display,
                (circle["x"], circle["y"]),
                circle["radius"],
                color,
                2
            )

        # Draw lines
        for line in lines:

            draw_tool(
                display,
                "line",
                line["x"],
                line["y"],
                line["length"],
                line["angle"]
            )

        cv2.imshow("Image", display)

        key = cv2.waitKeyEx(20)

        if key != -1:

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

            state["tool"] = current_tool

            print("Current frame:", current_frame)
            print("Current tool:", current_tool)

    cv2.destroyAllWindows()