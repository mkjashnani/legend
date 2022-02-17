import datetime
import time
import googleapiclient.discovery
import Telegram
def Time(YTET):
    Net=int(YTET)-time.time()
    return Net
def datetotimestamp(date):

    element = datetime.datetime.strptime(date,"%d/%m/%Y %H:%M:%S")
    timestamp1 = str(datetime.datetime.timestamp(element))
    timestamp_m=str()

    for i in range(0,int(len((timestamp1))-2)):
        timestamp_m=timestamp_m+str(timestamp1[i])
    return int(timestamp_m)

def YoutubeAlgo(videoid):
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    service = googleapiclient.discovery.build(
        API_NAME, API_VERSION,developerKey='AIzaSyCVIaRJ2Da61MKaWdArlO-I6hcA82ubg2w')
    part_string = 'contentDetails,statistics,snippet'
    video_ids = videoid
    response = service.videos().list(
            part=part_string,
            id=video_ids
        ).execute()
    return int(response.get('items')[0]['statistics']['viewCount'])
def Detailfetch(update):
    lastmsg = Telegram.get_last_chat_id_and_text(update)
    a = ''
    b = []
    for i in range(0, len(lastmsg)):
        if lastmsg[i] != ',':
            a = a + lastmsg[i]
        elif lastmsg[i] == ',':
            b.append(a)
            a = ''
    return b
