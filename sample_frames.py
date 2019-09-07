import cv2

video_capture = cv2.VideoCapture(2)
video_capture.set(3, 1920)
video_capture.set(4, 1080)

success, frame = video_capture.read()

index = 1
while(success):

    cv2.imshow("frame", frame)
    cv2.waitKey(10)

    if index % 100 == 0:
        id = int(index / 100)
        # cv2.imwrite("./frames/frame_%05d.jpg" % (id), frame)
    index += 1
    print(index)

    success, frame = video_capture.read()