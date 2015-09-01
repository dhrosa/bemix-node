import time, urllib, urllib2, json, sys
from VLCPlayer import Player
import config
from youtubeStreamer import YoutubeStreamer
def json_post(url, data):
    # passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    # passman.add_password(None, config.SERVER, config.SECRET_USERNAME, config.SECRET_PASSWORD)
    # urllib2.install_opener(urllib2.build_opener(urllib2.HTTPBasicAuthHandler(passman)))

    params = urllib.urlencode({'json': json.dumps(data)})
    req = urllib2.Request(url, params)
    req = urllib2.urlopen(url, params)
    res = req.read()
    return json.loads(res)

# if len(sys.argv) == 2:
#     NODENAME = sys.argv[1]
# else:
#     print "Usage: python bemix.py nodename"
#     sys.exit(0)

player = Player()
song = None
song_index = None
source = None
error =False
while True:
    time.sleep(.5)

    req = {'name': config.NODENAME}

    if player.loaded:
        req['position'] = player.position
    else:
        req['position'] = 0.0

    if (player.finished and song != None) or error:
        req['finished'] = song
        req['source']= source
        error = False

    try:
        res = json_post(config.SERVER_NOSSL + '/remix_player/tick', req)
    except urllib2.URLError, e:
        print e
        print config.SERVER_NOSSL + '/remix_player/tick'
        continue

    player.volume = res['volume']
    if song_index != res['song_index']:
        song = res['song']
        song_index = res['song_index']
        if song != None:
            source = res['song_source']
            if source == "local":
                print config.SERVER_NOSSL + "/remix_player/get/" + song
                player.load_url(config.SERVER_NOSSL + '/remix_player/get/' + song + "?.mp3")
            elif source == "youtube":
                try:
                    youtubeStr = YoutubeStreamer(song)
                    player.load_url(youtubeStr.get_stream_url())
                except:
                    req['finished'] = song
                    try:
                        error =True
                        
                    except urllib2.URLError, e:
                        print e
                        print config.SERVER_NOSSL + '/remix_player/tick'
                        continue
                    
    if song != None:
        if res['state'] == 'playing':
            player.play()
        elif res['state'] == 'paused':
            player.pause()
        if res['song']==None:
            song = None
            player.unload()

