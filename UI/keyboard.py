LEFT_ARROW = 2424832
RIGHT_ARROW = 2555904
def handle_key(key, current_frame, total_frames, current_tool="circle"):

    if key == ord('q'):
        return None

    elif key == RIGHT_ARROW:

        return min(
            current_frame + 1,
            total_frames - 1
        ), current_tool
    elif key == ord('c'):
        current_tool = "circle"
    

    elif key == ord('l'):
        current_tool = "line"

    elif key == LEFT_ARROW:

        return max(
            current_frame - 1,
            0
        ), current_tool

    return current_frame, current_tool