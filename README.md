# Bemix Node

## Configuration
First, configure the node:

    $ cp config_example.py config.py
    $ nano config.py

If you don't know the username and password, ask someone on hall or email miles@milessteele.com.

## Running
To run the node player that plays songs:

    $ python player.py

To run the button controller which connects the wall buttons to the music controls:

    $ python buttons.py

### Screens
Screens are useful for this sort of thing. Consider running these two processes in screens.

    $ screen -ls # list all screens on this host
    $ screen -R player # start or re-attach a screen called "player"

Press `ctrl-a` followed by `ctrl-d` to release a screen.
