#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This code is based on http://www.vision.is.tohoku.ac.jp/jp/course/ (Computer Vision Class)
'''

import cv2  # ライブラリを読み込む

cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')  # 学習済み顔識別器を読み込む

cv2.namedWindow('Camera')   # 'camera'というウインドウをつくる
cap = cv2.VideoCapture(0)   # 内蔵カメラ呼び出し

while 1:

    '''
    capオブジェクト(ビデオ)から，read()インスタンスを読み込み 
    statはreadできてるか(bool型)，imgは各フレームごとの画像
    '''
    stat, img = cap.read()  

    rects = cascade.detectMultiScale(img, 1.3, 4)   # 人と認識された領域の左上座標，その長さを返す．

    if len(rects) != 0: # 人と認識された場合
        '''
         (左上y座標，左上x座標，yの長さ，xの長さ)形式から 
         (左上y座標，左上x座標，右下y座標，右下x座標)形式に変換 
        '''
        rects[:, 2:] += rects[:, :2]    
        for x1, y1, x2, y2 in rects:
            '''
            実際に矩形を描画
            '''
            cv2.rectangle(img, (x1, y1), (x2, y2), (127, 255, 0), 2)

    cv2.imshow('camera', img)   # さっき作ったウィンドウ'camera'に画像を表示
    key = cv2.waitKey(10)       # キー入力待受

    if key == 0x1b:             # 0x1bキー(escキー) が押されたら終了
        break

cap.release()   #カメラ使用の解除
cv2.destroyAllWindows() #Windowの削除

