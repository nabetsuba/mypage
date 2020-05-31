from bottle import run, template, request, route
import os.path
from face_mosaic import face_mosaic

@route("/face_mosaic_main", method='GET')
def face_upload():
    #アップロード画面
    return template('face_mosaic')

@route("/face_mosaic_result", method='POST')
def face_upload_result():
    #画像をアップロード
    upload = request.files.get('upload')
    if upload and upload.file:
        raw = upload.file.read()  # This is dangerous for big files
        filename = upload.filename
        filepath = str("img/" + filename)

        #アップロードした画像をモザイク処理
        face_mosaic(filepath)

        if face_mosaic(filepath) != "失敗":
            return template('face_mosaic_result', result="モザイク処理に成功！ %s (%d bytes)." % (filename, len(raw))) + str(os.path.relpath(filename, start="face-mosaic"))
    return template('face_mosaic_result', result="モザイク処理に失敗！")

run(host='localhost', port=8080, reloader=True, debug=True)