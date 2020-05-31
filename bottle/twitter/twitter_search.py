import tweepy
from bottle import request

#認証キーの設定
CONSUMER_KEY = ""
CONSUMER_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def twitter_search():
    # OAuth認証
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # APIのインスタンスを生成
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # 特定のフォローを検索する
    fl_all = []
    word = str(request.query.word)
    username = str(request.query.username)
    followes_list = api.friends(screen_name=username, count=200)
    for follow in followes_list:
        fl = follow.name
        if word in fl:
            fl_all.append(fl)
    return fl_all