import cv2
import math


def mouse_callback(event, x, y, flags, param):

    tool = param["tool"]

    circles = param["circles"]
    lines = param["lines"]

    if tool == "circle":

        if event == cv2.EVENT_LBUTTONDOWN:

            selected = None

            for circle in circles:

                distance = math.sqrt(
                    (x - circle["x"]) ** 2 +
                    (y - circle["y"]) ** 2
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
                        "x": x,
                        "y": y,
                        "radius": 20
                    }
                )

        elif event == cv2.EVENT_MOUSEMOVE:

            if param["dragging"]:

                circle = param["selected_circle"]

                circle["x"] = x
                circle["y"] = y

        elif event == cv2.EVENT_LBUTTONUP:

            param["dragging"] = False
            param["selected_circle"] = None

        elif event == cv2.EVENT_MOUSEWHEEL:

            circle = param["selected_circle"]

            if circle is not None:

                if flags > 0:
                    circle["radius"] += 2
                else:
                    circle["radius"] = max(
                        5,
                        circle["radius"] - 2
                    )

    elif tool == "line":

        if event == cv2.EVENT_LBUTTONDOWN:

            lines.append((x, y))