import cv2
def openCVInitialize():
    try:
        import cv2
    except ImportError:
        print("OpenCV library not found. Installing...")
        try:
            import subprocess
            subprocess.check_call('pip3','install','opencv-python')
            print("OpenCV library has been installed successfully.")
            from cv2 import VideoCapture
        except Exception as e:
            print(f"Error installing OpenCV: {e}")
            exit()


def getFrame(b,w,h):
    videoCaptureObj = cv2.VideoCapture(0)

    if not videoCaptureObj.isOpened():
        print("Error: Could not open camera")
    else:
        videoCaptureObj.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        videoCaptureObj.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        videoCaptureObj.set(cv2.CAP_PROP_AUTO_EXPOSURE, 3)

        ret, frame = videoCaptureObj.read()

        frame = cv2.convertScaleAbs(frame, alpha=b, beta=0)

        if ret:
            cv2.imwrite('capturedFrame.jpg', frame)
            print("Frame captured and saved as 'capturedFrame.jpg'")
        else:
            print("Error: Failed to capture a frame.")
        videoCaptureObj.release()
    cv2.destroyAllWindows()
