from constants import FilterHenningChannelId, FilterHenningUserId, Api_Key


def main():
    playlists = getPlaylists("channel")
    likedvideos = getLikedVideos("channel")
    subscribedChannels = getSubscribedChannels("channel")
    print("Playlists of Channel")
    print(playlists)
    print("liked videos of channel")
    print(likedvideos)
    print("subscribed Channels")
    print(subscribedChannels)


"""
Youtube Api Waht do i Need to do?

Playlists:
GET https://www.googleapis.com/youtube/v3/playlists

videos aus Playlists:


Liked:

Channels:

Videos of channels:

"""


#Diese anfrage gibt die alle Playlists ids die ein Channel hat
f"https://www.googleapis.com/youtube/v3/playlists?key={Api_Key}&part=contentDetails&channelId={FilterHenningChannelId}&maxResults=10"
#dise anfrage gibt die die videos ids einer playlist du muss nurr die id bereit steleln
f"https://www.googleapis.com/youtube/v3/playlistItems?key={Api_Key}&part=contentDetails&playlistId=PLg7eNtqimWhyPUjoBZoWK-5VcIkQfuQ4x&maxResults=5"







#"id einer playlist"
"PLg7eNtqimWhxzVBsWVm-rxpECNuUiEJ9w"

#video id
"fc0V8GHYiOw"
#maybe ist das auch video id:¯\_(ツ)_/¯
"UExnN2VOdHFpbVdoeVBVam9CWm9XSy01VmNJa1FmdVE0eC4yODlGNEE0NkRGMEEzMEQy"