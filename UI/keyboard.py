import json


LEFT_ARROW = 2424832
RIGHT_ARROW = 2555904
DELETE_KEY = ord("d")
SAVE_KEY = ord("s")


def handle_key(
    key,
    current_frame,
    total_frames,
    current_tool="circle",
    state=None
):

    if key == ord('q'):
        return None

    elif key == RIGHT_ARROW:

        return min(
            current_frame + 1,
            total_frames - 1
        ), current_tool
    elif key == ord('c'):
        current_tool = "circle"

    elif key == SAVE_KEY:

        if state is not None:

            with open("annotations.json", "w", encoding="utf-8") as file:
                json.dump(state["annotations"], file, indent=4)

            print("Annotations saved to annotations.json")

    elif key == ord('l'):
        current_tool = "line"

    elif key == DELETE_KEY:

        if state is not None and state["dragging"]:

            state["circles"].remove(state["selected_circle"])
            state["selected_circle"] = None
            state["dragging"] = False

            return current_frame, current_tool

        if state is not None and state["dragging_line"]:

            state["lines"].remove(state["selected_line"])
            state["selected_line"] = None
            state["dragging_line"] = False

            return current_frame, current_tool

        return current_frame, current_tool

    elif key == LEFT_ARROW:

        return max(
            current_frame - 1,
            0
        ), current_tool

    return current_frame, current_tool