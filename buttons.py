import RPi.GPIO as GPIO
import time, urllib2, base64
import config

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

## setup pins
pins = [4,17,18,23,22]
names = {4:'back',17:'fwd',18:'down',23:'pause',22:'up'}
pianobar_cmds = {4:'' ,17:'n', 18:'(', 23:'p', 22:')'}
bemix_cmds = {4:'prev' ,17:'next', 18:'voldown', 23:'pause', 22:'volup'}
wait = 0
press = 0
delay = .25

print "Setting up pins..."
for pin in pins:
    GPIO.setup(pin,GPIO.IN)

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
            # pianowrite(pianobar_cmds[pin])
            bemix_remote_command(bemix_cmds[pin])
            wait = time.time() + delay
            press = pin

    time.sleep(.02)
