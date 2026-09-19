import cv2
from UI.draw import draw_tool


def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        if param["tool"] == "circle":

            param["circles"].append((x, y))

        elif param["tool"] == "line":

            param["lines"].append((x, y))