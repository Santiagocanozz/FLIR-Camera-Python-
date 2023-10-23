import EasyPySpin
import cv2


def main():
    cap = EasyPySpin.VideoCapture(0)

    if not cap.isOpened():
        print("Camera can't open\nexit")
        return -1

    cap.set(cv2.CAP_PROP_EXPOSURE, -1)  # -1 sets exposure_time to auto
    cap.set(cv2.CAP_PROP_GAIN, -1)  # -1 sets gain to auto

    while True:
        ret, frame = cap.read()
        # frame = cv2.cvtColor(frame, cv2.COLOR_BayerBG2BGR)  # for RGB camera demosaicing

        img_show = cv2.resize(frame, None, fx=0.25, fy=0.25)
        cv2.imshow("press q to quit", img_show)
        key = cv2.waitKey(30)
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()