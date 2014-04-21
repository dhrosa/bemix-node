from vlc import Instance, State, Media, ctypes
import time

class Player(object):
    def __init__(self):
        self.vlc_instance = Instance()
        self.vlc_player = self.vlc_instance.media_player_new()

    def load_url(self, url):
        self.vlc_player.set_mrl(url)

    def unload(self):
        null_media = object.__new__(Media)
        null_media._as_parameter_ = ctypes.c_void_p(0)
        self.vlc_player.set_media(null_media)

    def _get_volume(self):
        return self.vlc_player.audio_get_volume()
    def _set_volume(self, volume):
        self.vlc_player.audio_set_volume(volume)
    volume = property(_get_volume, _set_volume)

    def _get_position(self):
        return self.vlc_player.get_time() / 1000.0
    position = property(_get_position)

    def _get_loaded(self):
        return (self.vlc_player.get_state() == State.Opening or
                self.vlc_player.get_state() == State.Buffering or
                self.vlc_player.get_state() == State.Playing or
                self.vlc_player.get_state() == State.Paused or
                self.vlc_player.get_state() == State.Ended or
                self.vlc_player.get_state() == State.Stopped)
    loaded = property(_get_loaded)

    def _get_finished(self):
        return (self.vlc_player.get_state() == State.Ended or
                self.vlc_player.get_state() == State.Error or
                self.vlc_player.get_state() == State.Stopped)
    finished = property(_get_finished)

    def play(self):
        self.vlc_player.play()
    def pause(self):
        self.vlc_player.set_pause(True)

