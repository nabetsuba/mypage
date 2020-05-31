from bottle import route, run, template, request
from twitter_follow import twitter_follow as fl_all
from twitter_search import twitter_search as search

@route("/twitter_main", method='GET')
def twitter_main():
    return template("twitter")

@route("/twitter_result", method='GET')
def twitter_result():
    username = str(request.query.username)

    return template("twitter_result", result=search(), fl_all=fl_all(), username=username)

run(host='localhost', port=8080, reloader=True, debug=True)