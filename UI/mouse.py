import cv2
import math


def mouse_callback(event, x, y, flags, param):

    tool = param["tool"]

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
                    abs(y - line["y"]) < 10
                    and
                    left_edge <= x <= right_edge
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
                        "x": x,
                        "y": y,
                        "length": 30,
                        "angle": 0
                    }
                )

        elif event == cv2.EVENT_MOUSEMOVE:

            if param["dragging_line"]:

                line = param["selected_line"]

                line["x"] = x
                line["y"] = y

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

                        line["length"] += 5

                    else:

                        line["length"] = max(
                            10,
                            line["length"] - 5
                        )