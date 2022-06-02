import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Not open")
    exit()

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow("preview", frame)

        if cv2.waitkey(1) & 0xFF == ord("q"):
            break

except Exception as e:
    print("Exception occurred:", e)

finally:
    cap.release()
    cv2.destroyAllWindows()