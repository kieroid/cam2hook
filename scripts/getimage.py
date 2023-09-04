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
            import cv2
        except Exception as e:
            print(f"Error installing OpenCV: {e}")
            exit()


def getFrame():
    videoCaptureObj = cv2.VideoCapture(0)

    if not videoCaptureObj.isOpened():
        print("Error: Could not open camera")
    else:
        videoCaptureObj.set(cv2.CAP_PROP_BRIGHTNESS, 0.5)
        videoCaptureObj.set(cv2.CAP_PROP_CONTRAST, 0.5)
        videoCaptureObj.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)

        ret, frame = videoCaptureObj.read()

        if ret:
            cv2.imwrite('capturedFrame.jpg', frame)
            print("Frame captured and saved as 'capturedFrame.jpg'")
        else:
            print("Error: Failed to capture a frame.")
        videoCaptureObj.release()
    cv2.destroyAllWindows()
