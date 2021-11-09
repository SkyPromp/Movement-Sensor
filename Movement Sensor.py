import cv2 as cv
import winsound as ws

video = cv.VideoCapture(0)
_, prevframe = video.read()

while video.isOpened():
    ret, frame = video.read()

    if ret:
        cv.imshow("frame", frame)
        cv.imshow("prevframe", prevframe)
        if cv.matchTemplate(prevframe, frame, cv.TM_CCOEFF_NORMED)[0][0] < 0.99:
            cv.waitKey(1000)
            print("movement")
            ws.Beep(440, 200)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

    prevframe = frame

video.release()
cv.destroyAllWindows()
