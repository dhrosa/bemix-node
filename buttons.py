import RPi.GPIO as GPIO
import time, urllib2, base64
import config
import subprocess
import mplayer

blipper = mplayer.Player()

print "Starting button listener..."

## setup GPIO
GPIO.setmode(GPIO.BCM)
print "Pin address mode set to BCM."

# This can be use to control pianobar instead of bemix.
## open fifo
def pianowrite(cmd):
    with open('/home/pi/.config/pianobar/ctl','w') as f:
        f.write(cmd)

def bemix_remote_command(command):
    url = config.SERVER_NOSSL + "/remix/" + config.NODENAME + "/command/" + command
    print url
    req = urllib2.Request(url)
    base64string = base64.standard_b64encode('%s:%s' % (config.SECRET_USERNAME, config.SECRET_PASSWORD)).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)
    res = urllib2.urlopen(req)
    return res.read()

def blip():
    sndfile = "./blip.ogg"
    blipper.loadfile(sndfile)

## setup pins
BUTTON_LEFT = 4
BUTTON_UP = 22
BUTTON_RIGHT = 17
BUTTON_DOWN = 18
BUTTON_CENTER = 23

pin_names = {
    BUTTON_LEFT: 'back',
    BUTTON_RIGHT: 'forward',
    BUTTON_DOWN: 'down',
    BUTTON_UP: 'up',
    BUTTON_CENTER: 'pause'
}

pianobar_cmds = {
    BUTTON_LEFT: '',
    BUTTON_RIGHT:'n',
    BUTTON_DOWN:'(',
    BUTTON_CENTER:'p',
    BUTTON_UP:')'
}

bemix_cmds = {
    BUTTON_LEFT:'prev',
    BUTTON_RIGHT:'next',
    BUTTON_DOWN:'voldown',
    BUTTON_CENTER:'pause',
    BUTTON_UP:'volup'
}

wait = 0
press = 0
delay = .25

print "Setting up pins..."
for pin_number in pin_names.keys():
    GPIO.setup(pin_number,GPIO.IN)

print "Started polling."
frame = 0
while True:
    if (frame % 100) == 0:
        # print "Polling frame: " + frame
        pass
    frame += 1

    for pin in pins:
        if GPIO.input(pin) and (time.time()-wait >= 0 or pin != press):
            print names[pin]
            blip()
            # pianowrite(pianobar_cmds[pin])
            bemix_remote_command(bemix_cmds[pin])
            wait = time.time() + delay
            press = pin

    time.sleep(.02)
