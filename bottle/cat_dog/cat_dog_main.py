from bottle import route, run, template, request
import os.path
from cat_dog_judge import cat_dog_judge

@route("/cat_dog_main", method='GET')
def cat_dog_upload():
    return template("cat_dog")

@route("/cat_dog_result", method='POST')
def cat_dog_result():
    return template('cat_dog_result', result=cat_dog_judge())

run(host='localhost', port=8080, reloader=True, debug=True)