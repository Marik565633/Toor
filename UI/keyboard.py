def handle_key(key):
    '''Handle a key press event.'''
    if key == 'q':
        print("Quit key pressed.")
    else:
        print(f"Unhandled key: {key}")