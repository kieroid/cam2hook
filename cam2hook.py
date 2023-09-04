#IMAGE SETTINGS
#-------------------------------------------------------------------

#brightness? i don't really know what this means but i keep it around 2
brightness_factor = 2

#resolution of image (width, height)
resolution_width = 1920
resolution_height = 1080

#DISCORD SETTINGS
#-------------------------------------------------------------------

#webhook
webhook_url = ""

#other content (other than image.) do not include "image"
other_content = {

}

#SCRIPTS
#-------------------------------------------------------------------
from scripts import getimage
from scripts import sendhook

getimage.openCVInitialize()
sendhook.requestsInitialize()

getimage.getFrame(brightness_factor, resolution_width, resolution_height)
sendhook.sendHook(webhook_url,other_content)