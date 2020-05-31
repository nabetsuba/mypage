import matplotlib.pyplot as plt
import cv2, os
from mosaic import mosaic as mosaic

def face_mosaic(upimg):
    #カスケードファイルを指定して検出器を作成
    cascade_file = "haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_file)

    #画像を読み込んでグレートスケールに変換
    img = cv2.imread(upimg)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #顔認識を実行
    face_list = cascade.detectMultiScale(img_gray, minSize=(150, 150))

    #結果を確認
    if len(face_list) == 0:
        return "失敗"
        quit()

    #認識した部分にモザイクをかける
    for(x, y, w, h) in face_list:
        img = mosaic(img, (x, y, x+w, y+h), 10)

    #画像を保存と出力
    cv2.imwrite("img_mosaic/face-mosaic.jpg", img)
    return img