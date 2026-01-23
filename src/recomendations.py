import random


def getSubscribedChannels(userChannelId):
    pass
def getVideosofChannels(channelsidarr):
    pass

def getChannelName(channelid):
    pass
def getVideoLength(videoid):
    pass
def getChanneldBanner(channelid):
    pass  #maybe auch recource einer kanals da ist das banner ja mit dabei dann kann ich mir eine anfrage sparen
def formatVideos(videoUrl, thumbnail, channelname, channelBanner, length):
    pass 
    #hier soll einfach ein json geabaut werden welches dann ans front entübergeben werden kann
def sendVideostoFrontend(formatedVideosarr):
    pass

def loadVidoeRecomendations(userChannelId):
    channelsarr = getSubscribedChannels(userChannelId)
    videosarr = getVideosofChannels(channelsarr)
    random.shuffle(videosarr)
    for channel in channelsarr:
        pass
    
#ich denken an ein dict mit videoids als schlüßel und dahinter dann die bannerurl, channelname, lenghtofVideo, 
#wie sieht eine video recource aus weil ich muss die ja zuordnen


#wie sieht ein video aus was dann ans front end geschicket werden soll
#
#
#   thumbnail=thumbnailurl
#   src="https://www.youtube.com/embed/{video_id}
#   channelName=Name
#   Channeldbanner=bannerurl
#   videoLenght= 1:23       #wie machen keine sekunden because i don't care ob video 0:30:35 oder 0:30:50
#