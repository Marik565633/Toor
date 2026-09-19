import cv2

def draw_tool(image, tool, x, y, radius=15):
    if tool == "circle":
        cv2.circle(image, (x, y), radius, (0, 255, 0), 2)
    elif tool == "line":
        cv2.line(image, (x, y), (x + radius, y + radius), (0, 255, 0), 2)