import datetime
import time
import Youtube
import Telegram
import telesend
lv=0
lvt=0
while True:
    update=Telegram.get_json_from_url('https://api.telegram.org/bot5033997656:AAHcGq2QaeKPclqzNhP2msPxYVpaJiXgvx8/getupdates')
    alldel=Youtube.Detailfetch(update)
    print(alldel)
    Rview=alldel[0]
    ftime=alldel[1]
    ftimet = Youtube.datetotimestamp(ftime)
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
            if Youtube.YoutubeAlgo(videoid=video_id)>lv:
                nv=Youtube.YoutubeAlgo(videoid=video_id)-lv
                nt=time.time()-lvt
                nvc=nv/nt
                rt=ftimet-time.time()
                et=nvc*rt+Youtube.YoutubeAlgo(videoid=video_id)
                if int(et) > int(Rview):
                    print("SViews Will Meet ", "Expected Views:- ", et)
                    telesend.botmsg(str(("Views Will Meet ", "Expected Views:- ",et)))
                else:
                    telesend.botmsg(str(("Views Will Not Meet ", "Expected Views:- ", et)))
                    print("SViews Will Not Meet ", "Expected Views:- ", et)

                lv=Youtube.YoutubeAlgo(videoid=video_id)
                lvt=time.time()
                break


    try:
        while True:
            if Youtube.YoutubeAlgo(videoid=video_id)>a and a==0:
                a=int(Youtube.YoutubeAlgo(videoid=video_id))
                atime=time.time()
            elif Youtube.YoutubeAlgo(videoid=video_id) > a and b==0 and a!=0:
                b = int(Youtube.YoutubeAlgo(videoid=video_id))
                btime = time.time()
            elif Youtube.YoutubeAlgo(videoid=video_id) > a and Youtube.YoutubeAlgo(videoid=video_id) > b and c==0 and a!=0 and b!=0:
                c = int(Youtube.YoutubeAlgo(videoid=video_id))
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
                    telesend.botmsg(str(("Views Will Meet ", "Expected Views:- ", finalview)))
                else:
                    telesend.botmsg(str(("Views Will Not Meet ", "Expected Views:- ", finalview)))
                    print("Views Will Not Meet ", "Expected Views:- ", finalview)
                break
    except:
        pass

