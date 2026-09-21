import cv2
import math


def mouse_callback(event, x, y, flags, param):

    tool = param["tool"]
    scale = param["scale"]
    image_x = int(round(x / scale))
    image_y = int(round(y / scale))

    circles = param["circles"]
    lines = param["lines"]

    # =========================
    # CIRCLE TOOL
    # =========================
    if tool == "circle":

        if event == cv2.EVENT_LBUTTONDOWN:

            selected = None

            for circle in circles:

                distance = math.sqrt(
                    (image_x - circle["x"]) ** 2 +
                    (image_y - circle["y"]) ** 2
                )

                if distance <= circle["radius"]:

                    selected = circle
                    break

            if selected is not None:

                param["selected_circle"] = selected
                param["dragging"] = True

            else:

                circles.append(
                    {
                        "x": image_x,
                        "y": image_y,
                        "radius": int(round(20 / scale))
                    }
                )

        elif event == cv2.EVENT_MOUSEMOVE:

            if param["dragging"]:

                circle = param["selected_circle"]

                circle["x"] = image_x
                circle["y"] = image_y

        elif event == cv2.EVENT_LBUTTONUP:

            param["dragging"] = False
            param["selected_circle"] = None

        elif event == cv2.EVENT_MOUSEWHEEL:

            circle = param["selected_circle"]

            if circle is not None:

                if flags > 0:

                    circle["radius"] += int(round(2 / scale))

                else:

                    circle["radius"] = max(
                        int(round(5 / scale)),
                        circle["radius"] - int(round(2 / scale))
                    )

    # =========================
    # LINE TOOL
    # =========================
    elif tool == "line":

        if event == cv2.EVENT_LBUTTONDOWN:

            selected = None

            for line in lines:

                left_edge = line["x"] - line["length"] // 2
                right_edge = line["x"] + line["length"] // 2

                if (
                    abs(image_y - line["y"]) < int(round(10 / scale))
                    and
                    left_edge <= image_x <= right_edge
                ):

                    selected = line
                    break

            if selected is not None:

                print("LINE SELECTED")

                param["selected_line"] = selected
                param["dragging_line"] = True

            else:

                lines.append(
                    {
                        "x": image_x,
                        "y": image_y,
                        "length": int(round(30 / scale)),
                        "angle": 0
                    }
                )

        elif event == cv2.EVENT_MOUSEMOVE:

            if param["dragging_line"]:

                line = param["selected_line"]

                line["x"] = image_x
                line["y"] = image_y

        elif event == cv2.EVENT_LBUTTONUP:

            param["dragging_line"] = False
            param["selected_line"] = None

        elif event == cv2.EVENT_MOUSEWHEEL:

            line = param["selected_line"]

            if line is not None:

                # CTRL + Wheel = Rotate
                if flags & cv2.EVENT_FLAG_CTRLKEY:

                    if flags > 0:
                        line["angle"] += 5
                    else:
                        line["angle"] -= 5

                # Wheel only = Resize
                else:

                    if flags > 0:

                        line["length"] += int(round(5 / scale))

                    else:

                        line["length"] = max(
                            int(round(10 / scale)),
                            line["length"] - int(round(5 / scale))
                        )