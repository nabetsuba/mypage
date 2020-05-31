import tweepy
from bottle import request

#認証キーの設定
CONSUMER_KEY = ""
CONSUMER_SECRET_KEY = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

def twitter_timeline():
    # OAuth認証
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # APIのインスタンスを生成
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # 指定したユーザーのタイムラインを見る
    username = str(request.query.username)
    tl_all = []
    timelines = api.user_timeline(screen_name=username, count=10)
    for timeline in timelines:
        tl = timeline.user.name + timeline.text + '<<>>'
        tl_all.append(tl)
    return tl_all