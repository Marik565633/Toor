import cv2

from toor_distance.image_processor import load_image
from UI.keyboard import handle_key
from UI.mouse import mouse_callback
from UI.draw import draw_tool


def display_image(image_paths):

    current_frame = 0
    scale = 0.4
    current_tool = "circle"

    annotations = {}
    frame_annotations = annotations.setdefault(
        current_frame,
        {"circles": [], "lines": []}
    )

    state = {
        "annotations": annotations,
        "scale": scale,
        "circles": frame_annotations["circles"],
        "lines": frame_annotations["lines"],
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

        frame_annotations = annotations.setdefault(
            current_frame,
            {"circles": [], "lines": []}
        )
        state["circles"] = frame_annotations["circles"]
        state["lines"] = frame_annotations["lines"]

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
        for circle in state["circles"]:

            color = (0, 255, 0)

            if state["selected_circle"] is circle:
                color = (0, 0, 255)

            cv2.circle(
                display,
                (
                    int(round(circle["x"] * scale)),
                    int(round(circle["y"] * scale))
                ),
                max(1, int(round(circle["radius"] * scale))),
                color,
                2
            )

        # Draw lines
        for line in state["lines"]:

            draw_tool(
                display,
                "line",
                int(round(line["x"] * scale)),
                int(round(line["y"] * scale)),
                int(round(line["length"] * scale)),
                line["angle"]
            )

        cv2.imshow("Image", display)

        key = cv2.waitKeyEx(20)

        if key != -1:

            result = handle_key(
                key,
                current_frame,
                len(image_paths),
                current_tool,
                state
            )

            if result is None:
                break

            previous_frame = current_frame
            current_frame = result[0]
            current_tool = result[1]

            state["tool"] = current_tool

            if current_frame != previous_frame:
                state["selected_circle"] = None
                state["dragging"] = False
                state["selected_line"] = None
                state["dragging_line"] = False

            print("Current frame:", current_frame)
            print("Current tool:", current_tool)

    cv2.destroyAllWindows()