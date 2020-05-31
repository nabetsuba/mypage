import tweepy
from bottle import request

#認証キーの設定
CONSUMER_KEY = ""
CONSUMER_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def twitter_follow():
    # OAuth認証
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # APIのインスタンスを生成
    api = tweepy.API(auth, wait_on_rate_limit=True)

    #指定したユーザーのフォローの情報を見る
    username = str(request.query.username)
    fl_all =[]
    followes_list = api.friends(screen_name=username, count=200)
    for follow in followes_list:
        fl_all.append(follow.name)
    return fl_all