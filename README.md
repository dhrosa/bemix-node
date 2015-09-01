# Bemix Node

A bemix node is one of the stations that plays music from bemix.

## Configuration
First, configure your node:

    $ cp config_example.py config.py
    $ nano config.py

And install pafy:
    $pip install pafy

If you don't know the username and password, ask someone on hall or email miles@milessteele.com.

## Starting a Node
### Player
The player plays music from the bemix server.
It can run on almost anything, and only requires that VLC is installed.

To run the node player that plays songs:

    $ python player.py

### Buttons
Bemix has sweet buttons on the wall in the bathrooms that can control playback.
To enable the buttons, you will need to be running this from a raspberry pi (for this version).

Plug the board in the ceiling into the pi and run:

    $ sudo python buttons.py

(buttons needs sudo because it accesses the gpio pins)

### Screens
Screens are useful for this sort of thing. Consider running these two processes in screens.

    $ screen -ls # list all screens on this host
    $ screen -R player # start or re-attach a screen called "player"

Press `ctrl-a` followed by `ctrl-d` to release a screen.
