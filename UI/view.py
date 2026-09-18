import cv2

def display_image(image):

    print("Entering display_image")

    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    print("Converted to BGR")

    h, w = image_bgr.shape[:2]

    scale = 0.4

    new_w = int(w * scale)
    new_h = int(h * scale)

    print("New size:", new_w, new_h)

    display = cv2.resize(
        image_bgr,
        (new_w, new_h),
        interpolation=cv2.INTER_AREA
    )

    print("Resize complete")

    while True:

        cv2.imshow("Image", display)

        key = cv2.waitKey(20)

        if key == ord('q'):
            break

    cv2.destroyAllWindows()