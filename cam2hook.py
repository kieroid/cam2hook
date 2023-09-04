try:
    from scripts import getimage
    from scripts import sendhook
    print("Initialized Scripts.")
except ImportError:
    print("Scripts unable to initialize.")
    exit()

getimage.openCVInitialize()
getimage.getFrame()

