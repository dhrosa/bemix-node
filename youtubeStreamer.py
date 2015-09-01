import pafy

class YoutubeStreamer:
    def __init__(self, url):
        self.youtube_url = url
        video = pafy.new(self.youtube_url) # takes a sec to get/parse
        self.stream_url = video.getbestaudio().url
    
    def get_stream_url(self):
        return self.stream_url
    def get_youtube_url(self):
        return self.youtube_url
