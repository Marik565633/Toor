import cv2
import math


def draw_tool(image, tool, x, y, size=15, angle=0):

    if tool == "circle":

        cv2.circle(
            image,
            (x, y),
            size,
            (0, 255, 0),
            2
        )

    elif tool == "line":

        radians = math.radians(angle)

        dx = (size / 2) * math.cos(radians)
        dy = (size / 2) * math.sin(radians)

        start_point = (
            int(x - dx),
            int(y - dy)
        )

        end_point = (
            int(x + dx),
            int(y + dy)
        )

        cv2.line(
            image,
            start_point,
            end_point,
            (0, 255, 0),
            2
        )