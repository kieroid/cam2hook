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
webhook_url = "https://discord.com/api/webhooks/1148073673807372418/6zUyqcpn-l4MvNX_l1oAn36xlk5U2n_6_3r72DVznq9BzQDm5gM6kYJCIInY0Y5rZumA"

# other content (other than image.) do not include "image"
other_content = {
    "username":  "24/7 kieran dox stream",
    "avatar_url": "https://shellfish.racing/k/images/lobster.png",
    "content": str(datetime.datetime.now().strftime("%B %d, %Y, at %H:%M"))
}

# SCRIPTS
# -------------------------------------------------------------------
from scripts import getimage
from scripts import sendhook

getimage.openCVInitialize()
sendhook.requestsInitialize()

getimage.getFrame(brightness_factor, resolution_width, resolution_height)
sendhook.sendHook(webhook_url, other_content)
