import cv2

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Left click at:", x, y)

    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Right click at:", x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        print("Mouse moved to:", x, y)