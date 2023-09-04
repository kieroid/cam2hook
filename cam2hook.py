import datetime
# IMAGE SETTINGS
# -------------------------------------------------------------------

# brightness? i don't really know what this means but i keep it around 2
brightness_factor = 2

# resolution of image (width, height)
resolution_width = 1920
resolution_height = 1080

# DISCORD SETTINGS
# -------------------------------------------------------------------

# webhook
webhook_url = open("insert_webhooks_here").read()

# other content (other than image.) do not include "image"
other_content = {
    "username":  "24/7 kieran dox stream",
    "avatar_url": "https://shellfish.racing/k/images/lobster.png",
    "content": str(datetime.datetime.now().strftime("%B %d, %Y, at %H:%M"))+"\n\n"
}

# SCRIPTS
# -------------------------------------------------------------------
from scripts import getimage
from scripts import sendhook

getimage.openCVInitialize()
sendhook.requestsInitialize()

getimage.getFrame(brightness_factor, resolution_width, resolution_height)
sendhook.sendHook(webhook_url, other_content)
