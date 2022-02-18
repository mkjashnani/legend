import datetime
import time
import googleapiclient.discovery
import requests
import json
lv=0
lvt=0

TOKEN = "5064671174:AAFTdDwyLtGK55K2k0wIJsioJsV5pzfcUPE"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    #text = updates["result"][last_update]["message"]["text"]
    text = updates['result'][-1]['message']['text']
    #chat_id = updates["result"][2]["message"]["chat"]["id"]
    return (text)


def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)

def botmsg(bot_message):
    bot_token = '5033997656:AAHcGq2QaeKPclqzNhP2msPxYVpaJiXgvx8'
    bot_chatID = '2025063834'#LEGEND
    #bot_chatID1 = '1688134885'#rio
    #bot_chatID1 = '548521105'#siva
    #314516752
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    #send_text1='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID1 + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    # response1 = requests.get(send_text1)
    return response.json()
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
    lastmsg =  get_last_chat_id_and_text(update)
    a = ''
    b = []
    for i in range(0, len(lastmsg)):
        if lastmsg[i] != ',':
            a = a + lastmsg[i]
        elif lastmsg[i] == ',':
            b.append(a)
            a = ''
    return b

while True:
    botmsg("hey")
    update= get_json_from_url('https://api.telegram.org/bot5033997656:AAHcGq2QaeKPclqzNhP2msPxYVpaJiXgvx8/getupdates')
    alldel= Detailfetch(update)
    print(alldel)
    Rview=alldel[0]
    ftime=alldel[1]
    ftimet =  datetotimestamp(ftime)
    video_id=alldel[2]
    a=0
    atime=0
    b=0
    btime=0
    c=0
    ctime=0
    #
    if lv!=0 and lvt!=0:
        while True:
            if  YoutubeAlgo(videoid=video_id)>lv:
                nv= YoutubeAlgo(videoid=video_id)-lv
                nt=time.time()-lvt
                nvc=nv/nt
                rt=ftimet-time.time()
                et=nvc*rt+ YoutubeAlgo(videoid=video_id)
                if int(et) > int(Rview):
                    print("SViews Will Meet ", "Expected Views:- ", et)
                    botmsg(str(("Views Will Meet ", "Expected Views:- ",et)))
                else:
                    botmsg(str(("Views Will Not Meet ", "Expected Views:- ", et)))
                    print("SViews Will Not Meet ", "Expected Views:- ", et)

                lv= YoutubeAlgo(videoid=video_id)
                lvt=time.time()
                break


    try:
        while True:
            if  YoutubeAlgo(videoid=video_id)>a and a==0:
                a=int( YoutubeAlgo(videoid=video_id))
                atime=time.time()
            elif  YoutubeAlgo(videoid=video_id) > a and b==0 and a!=0:
                b = int( YoutubeAlgo(videoid=video_id))
                btime = time.time()
            elif  YoutubeAlgo(videoid=video_id) > a and  YoutubeAlgo(videoid=video_id) > b and c==0 and a!=0 and b!=0:
                c = int( YoutubeAlgo(videoid=video_id))
                lv=c

                ctime = time.time()
                lvt=ctime
            elif a!=0 and b!=0 and c!=0:
                netview=int(c)-int(b)
                nettime=int(ctime)-int(btime)
                nettimef=nettime/60
                cvr=netview/nettimef
                print(cvr)
                rtime=(ftimet-ctime)/60
                finalview=cvr*rtime+c
                if int(finalview)>int(Rview):
                    print("Views Will Meet ","Expected Views:- ",finalview)
                    botmsg(str(("Views Will Meet ", "Expected Views:- ", finalview)))
                else:
                    botmsg(str(("Views Will Not Meet ", "Expected Views:- ", finalview)))
                    print("Views Will Not Meet ", "Expected Views:- ", finalview)
                break
    except:
        pass

