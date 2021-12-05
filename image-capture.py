import cv2

camera = cv2.VideoCapture(0)

cv2.namedWindow("capture-image")

counter = 0

while True:
    ret, frame = camera.read()
    if not ret:
        print("failed to capture frame")
        break
    cv2.imshow("capture-image", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "captured-image_{}.png".format(counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        counter += 1

camera.release()

cv2.destroyAllWindows()