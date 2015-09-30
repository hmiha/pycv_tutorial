#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
***注意***

1. numpy_arrayに画像を格納した場合，座標系は[y, x]になります．
numpy_arrayはもともと行列演算ライブラリなので，行・列という順で数えるためかと．
ただし，OpenCVの関数の引数には(x, y)と与える場合もあるので，
使う関数のドキュメントを参照してください．

2. print img[y, x] で出力される色は[B, G, R]の順番です．
よく[R, G, B]と間違えるので注意．
'''

import cv2
import numpy as np  # 行列演算のライブラリ

img = cv2.imread('lena.bmp', 1) # 1:カラー画像, 0:モノクロ画像, -1:そのまま

print type(img)     #データ形式を出力．numpy_ndarrayと出力されます．

x = raw_input('input x:')   # キーボード入力
y = raw_input('input y:')   # 

print img[y, x] 

