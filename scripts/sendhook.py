import requests
import os


def requestsInitialize():
    try:
        import requests
    except ImportError:
        print("requests not found. Installing...")
        try:
            import subprocess
            subprocess.check_call('pip3', 'install', 'requests')
            print("requests has been installed successfully.")
            import requests
        except Exception as e:
            print(f"Error installing requests: {e}")
            exit()


def sendHook(url, payload):
    with open("capturedFrame.jpg", 'rb') as f:
        image_data = f.read()
        payload["file"] = ("image.jpg", image_data)

    response = requests.post(url, files=payload)
    if response.status_code == 204:
        print("Image sent successfully")
    else:
        print(f"Error sending image: {response.status_code}")
