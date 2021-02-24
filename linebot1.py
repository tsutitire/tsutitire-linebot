from flask import Flask, request, abort
 
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage,
)
import os
import random
import asyncio
import subprocess
import random
import urllib3
import urllib.error
import urllib.request
import urllib.parse
import json
import datetime
import time
import tweepy
import bs4
from bs4 import BeautifulSoup
import codecs
app = Flask(__name__)
 
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]
 
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)
 
 
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
 
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def uranai():
    if True == True:
        uranai = 0
        uranai = random.randrange(10)
        if uranai == 0:
            return '大凶です^^'
        if uranai == 1:
            return '凶くらいです^^'
        if uranai == 2:
            return '中凶です^^'
        if uranai == 3:
            return '小凶です^^'
        if uranai == 4:
            return 'なんともないでしょう^^'
        if uranai == 5:
            return '小吉です^^'
        if uranai == 6:
            return '末吉です^^'
        if uranai == 7:
            return '中吉です^^'
        if uranai == 8:
            return '吉です^^'
        if uranai == 9:
            return '大吉です^^'
        if uranai == 10:
            return '見事枠にない1つに当たりましたね！大凶です！'    

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    messagetex = event.message.text
    if messagetex.startswith("dice"):
        spmes = messagetex.split()
        if len(spmes) == 2:
            dice_rand = random.randint(1,int(spmes[1]))
            rep_mes = "さいころの結果：" + str(dice_rand)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=rep_mes))
        else:
            dice_rand = random.randint(1,6)
            rep_mes = "さいころの結果：" + str(dice_rand)
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=rep_mes))
    
    if messagetex.startswith("janken"):
        janken = random.randrange(3)
        jankenws = messagetex.split()
        jankenw = jankenws[1]
        if jankenw == "r":
            if janken == 1:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="グーとグーで、あいこですね"))
            elif janken == 2:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="グーとパーで、ボクの勝ちです！(｀・ω・´)"))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="グーとチョキで、キミの勝ちです！(´・ω・`)"))
        elif jankenw == "p":
            if janken == 1:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="パーとグーで、キミの勝ちです！(´・ω・`)"))
            elif janken == 2:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="パーとパーで、あいこですね"))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="パーとチョキで、ボクの勝ちです！(｀・ω・´)"))
        elif jankenw == "s":
            if janken == 1:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="チョキとグーで、ボクの勝ちです！(｀・ω・´)"))
            elif janken == 2:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="チョキとパーで、キミの勝ちです！(´・ω・`)"))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="チョキとチョキで、あいこですね"))
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="janken r/p/s で指定してくださいよぉ...(-_-;)"))

    if messagetex.startswith("omikuzi"):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=uranai()))
        
    if messagetex.startswith("bitcoin"):
        http = urllib3.PoolManager()
        link = 'https://api.coindesk.com/v1/bpi/currentprice/JPY.json'
        r = http.request('GET',link)
        rr = str(r.data)
        print(rr)
        rind1 = rr.find('"rate"')
        rind2 = rr.find('","',rind1)
        rind3 = rr.find('"rate"',rind2)
        rind4 = rr.find('","',rind3)
        print(str(rind1) + "a" + str(rind2) + "b" + str(rind3) + "c" + str(rind4))
        rdat1 = rr[(rind1 + 8):(rind2 - 1)]
        rdat2 = rr[(rind3 + 8):(rind4 - 1)]
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="USD: " + rdat1 + " $ and JPY: " + rdat2 + "￥"))
    if messagetex.startswith("skin1"):
        http = urllib3.PoolManager()
        MCID2 = messagetex.split()
        MCID = MCID2[1]
        MCID = 'https://api.mojang.com/users/profiles/minecraft/' + MCID
        r = http.request('GET',MCID)
        findr = str(r.data)
        indA = findr.find(',')
        findr = findr[(indA + 7):-3]
        findr = findr[0:8] + '-' + findr[8:12] + '-' + findr[12:16] + '-' + findr[16:20] + '-' + findr[20:]
        spmes = messagetex.split()
        UUID = findr
        UUID = 'https://crafatar.com/renders/body/' + UUID + "?overlay"
        r = http.request('GET',UUID)
        url = UUID
        img_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url,
        )
        line_bot_api.reply_message(event.reply_token,img_message)
        
    if messagetex.startswith("skin2"):
        http = urllib3.PoolManager()
        spmes = messagetex.split()
        UUID = spmes[1]
        UUID = 'https://minotar.net/avatar/' + UUID
        r = http.request('GET',UUID)
        url = UUID
        img_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url,
        )
        line_bot_api.reply_message(event.reply_token,img_message)
        
    if messagetex.startswith("skin3"):
        http = urllib3.PoolManager()
        spmes = messagetex.split()
        UUID = spmes[1]
        UUID = 'https://minotar.net/skin/' + UUID
        r = http.request('GET',UUID)
        url = UUID
        img_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url,
        )
        line_bot_api.reply_message(event.reply_token,img_message)
        
    if messagetex.startswith("slot"):
        if messagetex.startswith("slot"):
            slot1 = 0
            slot2 = 0
            slot3 = 0
            slot4 = 0
            slot5 = 0
            slot6 = 0
            slot7 = 0
            slot8 = 0
            slot9 = 0
            slot_hit = 0
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot1 = "♡"
            elif slot_random == 1:
                slot1 = "💴"
            elif slot_random == 2:
                slot1 = "🀄"
            elif slot_random == 3:
                slot1 = "🍎"
            else:
                slot1 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot2 = "♡"
            elif slot_random == 1:
                slot2 = "💴"
            elif slot_random == 2:
                slot2 = "🀄"
            elif slot_random == 3:
                slot2 = "🍎"
            else:
                slot2 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot3 = "♡"
            elif slot_random == 1:
                slot3 = "💴"
            elif slot_random == 2:
                slot3 = "🀄"
            elif slot_random == 3:
                slot3 = "🍎"
            else:
                slot3 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot4 = "♡"
            elif slot_random == 1:
                slot4 = "💴"
            elif slot_random == 2:
                slot4 = "🀄"
            elif slot_random == 3:
                slot4 = "🍎"
            else:
                slot4 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot5 = "♡"
            elif slot_random == 1:
                slot5 = "💴"
            elif slot_random == 2:
                slot5 = "🀄"
            elif slot_random == 3:
                slot5 = "🍎"
            else:
                slot5 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot6 = "♡"
            elif slot_random == 1:
                slot6 = "💴"
            elif slot_random == 2:
                slot6 = "🀄"
            elif slot_random == 3:
                slot6 = "🍎"
            else:
                slot6 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot7 = "♡"
            elif slot_random == 1:
                slot7 = "💴"
            elif slot_random == 2:
                slot7 = "🀄"
            elif slot_random == 3:
                slot7 = "🍎"
            else:
                slot7 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot8 = "♡"
            elif slot_random == 1:
                slot8 = "💴"
            elif slot_random == 2:
                slot8 = "🀄"
            elif slot_random == 3:
                slot8 = "🍎"
            else:
                slot8 = "🎮"
            slot_random = random.randrange(5)
            if slot_random == 0:
                slot9 = "♡"
            elif slot_random == 1:
                slot9 = "💴"
            elif slot_random == 2:
                slot9 = "🀄"
            elif slot_random == 3:
                slot9 = "🍎"
            else:
                slot9 = "🎮"
    
            if slot1 == slot2 and slot2 == slot3:
                slot_hit = slot_hit + 1
            if slot4 == slot5 and slot5 == slot6:
                slot_hit = slot_hit + 1
            if slot7 == slot8 and slot8 == slot9:
                slot_hit = slot_hit + 1
            if slot1 == slot4 and slot4 == slot7:
                slot_hit = slot_hit + 1
            if slot2 == slot5 and slot5 == slot8:
                slot_hit = slot_hit + 1
            if slot3 == slot6 and slot6 == slot9:
                slot_hit = slot_hit + 1
            if slot1 == slot5 and slot5 == slot9:
                slot_hit = slot_hit + 1
            if slot3 == slot5 and slot5 == slot7:
                slot_hit = slot_hit + 1
           
            if slot_hit == 0:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="==========\n" +\
                                                                             "|" + str(slot1) + "|" + str(slot2) + "|" + str(slot3) + "|\n" +\
                                                                                 "|" + str(slot4) + "|" + str(slot5) + "|" + str(slot6) + "|\n" +\
                                                                                     "|" + str(slot7) + "|" + str(slot8) + "|" + str(slot9) + "|\n" +\
                                                                                         "==========\n" +\
                                                                                             "全部外れました"))
            if slot_hit != 0:                                                                              
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="==========\n" +\
                                                                             "|" + str(slot1) + "|" + str(slot2) + "|" + str(slot3) + "|\n" +\
                                                                                 "|" + str(slot4) + "|" + str(slot5) + "|" + str(slot6) + "|\n" +\
                                                                                     "|" + str(slot7) + "|" + str(slot8) + "|" + str(slot9) + "|\n" +\
                                                                                         "==========\n" +\
                                                                                             str(slot_hit) + "列当たりました！"))
                                                                                             
        
    if messagetex.startswith("twitter"):
        spmes = messagetex.split()
        args = spmes
        if len(args) == 1:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="引数が少なすぎます。何ができるかを確認するには；twitter help"))
            pass
        if args[1] == "help":
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text="twitter search <アカウントID> <遡るツイート数> : その人のツイートを調べられます\ntwitter search-all <検索キーワード> <遡るツイート数>:ツイートを調べられます\ntwitter osi/osi2/osi3 検索ワード[3の場合ユーザーid]"))
        if args[1] == "search":
            if len(args) == 4:
                
                
                
                CONSUMER_KEY = os.environ["CONSUMER_KEY"]
                
                CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
                
                ACCESS_KEY = os.environ["ACCESS_KEY"]
                
                ACCESS_SECRET = os.environ["ACCESS_SECRET"]
                
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                
                api = tweepy.API(auth)
                
                
                #api.update_status("テストメッセージを投稿してみてます、つちさんです。")
                
                Account = args[2] #取得したいユーザーのユーザーIDを代入
                try:
                    if int(args[3]) >= 30:
                        args[3] = 30
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="取得ツイート数は半角数字で入力してくださいな それか数がおかしいか多すぎるかも？"))
                    pass
                
                try:
                    tweets = api.user_timeline(Account, count=int(args[3]), page=1)
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="名前とか、間違ってませんか？"))
                    pass
                num = 1 #ツイート数を計算するための変数
                sendtexts = ""
                for tweet in tweets:
                    #print('twid : ', tweet.id)               # tweetのID
                    #print('user : ', tweet.user.screen_name)  # ユーザー名
                    #print('date : ', tweet.created_at)      # 呟いた日時
                    #print('favo : ', tweet.favorite_count)  # ツイートのいいね数
                    #print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
                    #print('ツイート数 : ', num) # ツイート数
                    #print('='*80) # =を80個表示
                    sendtexts = sendtexts + "contents： " + str(tweet.text) + "time： " + str(tweet.created_at) + " likes/retweet： " + str(tweet.favorite_count) + "/" + str(tweet.retweet_count) + "\n"
                    num += 1 # ツイート数を計算
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendtexts))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="引数が不正です"))
                
        if args[1] == "search-all":
            if len(args) == 4:
  
                CONSUMER_KEY = os.environ["CONSUMER_KEY"]
                
                CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
                
                ACCESS_KEY = os.environ["ACCESS_KEY"]
                
                ACCESS_SECRET = os.environ["ACCESS_SECRET"]
                
                auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
                
                auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
                
                api = tweepy.API(auth)
                
                
                try:
                    if int(args[3]) >= 30:
                        args[3] = 30
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="取得ツイート数は半角数字で入力してくださいな それか数がおかしいか多すぎるかも？"))
                    pass
                
                try:
                    tweets = api.search(q=args[2], count=int(args[3]))
                except:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text="引数とか、間違ってませんか？"))
                    pass
                num = 1 #ツイート数を計算するための変数
                sendtexts = ""
                for tweet in tweets:
                    #print('twid : ', tweet.id)               # tweetのID
                    #print('user : ', tweet.user.screen_name)  # ユーザー名
                    #print('date : ', tweet.created_at)      # 呟いた日時
                    #print('favo : ', tweet.favorite_count)  # ツイートのいいね数
                    #print('retw : ', tweet.retweet_count)  # ツイートのリツイート数
                    #print('ツイート数 : ', num) # ツイート数
                    #print('='*80) # =を80個表示
                    sendtexts = sendtexts + "contents： " + str(tweet.text) + "time： " + str(tweet.created_at) + " likes/retweet： " + str(tweet.favorite_count) + "/" + str(tweet.retweet_count) + "\n"
                    num += 1 # ツイート数を計算
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text=sendtexts))
            else:
                line_bot_api.reply_message(event.reply_token,TextSendMessage(text="引数が不正です"))
        
        if args[1] == "osi":
            CONSUMER_KEY = os.environ["CONSUMER_KEY"]
            
            CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
            
            ACCESS_KEY = os.environ["ACCESS_KEY"]
            
            ACCESS_SECRET = os.environ["ACCESS_SECRET"]
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            media_url_list = []
            download_url_list = []
            max_id = None
            term = messagetex[12:]
            for i in range(20):
                rpp = 100
                if max_id:
                    search_result = api.search(q=term, rpp=rpp, max_id=max_id, result_type="mixed")
                else:
                    search_result = api.search(q=term, rpp=rpp, result_type="mixed")
                for result in search_result:
                    if "media" in result.entities:
                        for media in result.entities['media']:
                            url = media['media_url_https']
                            if url not in media_url_list:
                                media_url_list.append(url)
                                download_url_list.append(url)
                max_id = result.id
            send_text = ""
            count = 0
            for i in media_url_list:
                count = count + 1
                send_text = send_text + str(count) + " ： " + i + " \n\n"
                
            #aaaa
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=send_text))
        if args[1] == "osi2":
            CONSUMER_KEY = os.environ["CONSUMER_KEY"]
            
            CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
            
            ACCESS_KEY = os.environ["ACCESS_KEY"]
            
            ACCESS_SECRET = os.environ["ACCESS_SECRET"]
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            media_url_list = []
            download_url_list = []
            max_id = None
            term = messagetex[13:]
            for i in range(20):
                rpp = 100
                if max_id:
                    search_result = api.search(q=term, rpp=rpp, max_id=max_id)
                else:
                    search_result = api.search(q=term, rpp=rpp)
                for result in search_result:
                    if "media" in result.entities:
                        for media in result.entities['media']:
                            url = media['media_url_https']
                            if url not in media_url_list:
                                media_url_list.append(url)
                                download_url_list.append(url)
                max_id = result.id
            send_text = ""
            count = 0
            for i in media_url_list:
                count = count + 1
                send_text = send_text + str(count) + " ： " + i + " \n\n"
                
                
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=send_text))
        if args[1] == "osi3":
            CONSUMER_KEY = os.environ["CONSUMER_KEY"]
            
            CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
            
            ACCESS_KEY = os.environ["ACCESS_KEY"]
            
            ACCESS_SECRET = os.environ["ACCESS_SECRET"]
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            user_name = args[2]
            results = api.user_timeline(screen_name=user_name, count="1")
            for result in results:
                psid = result.id
                
            result_url = []
            count = 100
            for i in range(0, 2):
                results = api.user_timeline(screen_name=user_name, count=count, max_id=psid)
                psid = results[-1].id
                for result in results:
                    if 'media' in result.entities:
                        judg = 'RT @' in result.text
                        if judg == False:
                            for media in result.extended_entities['media']:
                                result_url.append(media['media_url'])
            
            send_text = ""
            count = 0
            for i in result_url:
                count = count + 1
                send_text = send_text + str(count) + " ： " + i + " \n\n"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=send_text))
        if args[1] == "getret":
            CONSUMER_KEY = os.environ["CONSUMER_KEY"]
            
            CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
            
            ACCESS_KEY = os.environ["ACCESS_KEY"]
            
            ACCESS_SECRET = os.environ["ACCESS_SECRET"]
            auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
            api = tweepy.API(auth)
            
            strings = ""
            
            lstweets = api.user_timeline(args[2],count=5)
            for j in lstweets:
                firstTweet = j
                
    
                results = api.retweets(firstTweet.id)
                retweeters = []
                appendtext = "tweet: \n" + firstTweet.text + "\n\n" 
                for i in results:
                    
                    retweeters.append(i.user.screen_name)
                for k in reversed(retweeters):
                    appendtext = appendtext + k + "\n"
            
                strings = strings + appendtext + "\n\n"
            
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=strings))
            
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="コマンドが間違ってるか、たぶん違うやつですね。ヘルプ貼りますね～\n\n\ dice [最大数]:1～最大数まで(指定しなければ6)の範囲のさいころをふります！\n\njanken r/p/s:じゃんけんができます！\n\nomikuzi:おみくじが引けます\n\nbitcoin:ビットコインのレートを取得できます\n\nskin1/2/3 mcid:マイクラのスキンを取得できます\n\nslot:スロットを回せます!\n\ntwitter help:twitterコマンドのヘルプが見れます、詳細はそこで！")) #ここでオウム返しのメッセージを返します。
        
    
    
    
# ポート番号の設定
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
