#coding: utf-8

import numpy as np
import cv2

arr = np.genfromtxt("sample.csv", delimiter=",")
cnt=0
rgba_all=[] #RGBAで一区切りにした配列
rgba=[]
for x in arr: #一次元配列をRGBAで一区切りにする
	if cnt==4:
		cnt=0
		rgba=[]
	rgba.append(x)
	cnt+=1
	if len(rgba)==4:
		#print (rgba)
		rgba_all.append(rgba)
i=0
"""#色の指定
r=103
g=88
b=85
for x in rgba_all: #1pxごとのRGBAを取り出して指定色をカウント
	if (x[0]==r and x[1]==g and x[2]==b): #指定色の場合は加算
		i+=1
print ("(R,G,B)=(%d,%d,%d)は%d個存在します" %(r,g,b,i))
"""
#生成する画像のサイズ
cols = 160
rows = 120

#イメージ生成
image = np.zeros((rows, cols, 3), np.uint8)
div = 160 # 縦横の分割数
w = int(cols / div) # 分割された領域の横幅
h = int(rows / div) # 分割された領域の縦幅

w=4
h=4

cnt_w=0
cnt_h=0
for rgba in rgba_all:
	print(rgba)
	image[h*cnt_h:h*(cnt_h*4+4),w*cnt_w:w*(cnt_w*4+4)] = [int(rgba[2]),int(rgba[1]),int(rgba[0])]
	cnt_w+=1
	if cnt_w!=0 and cnt_w%160==0:
		cnt_w=0
		cnt_h+=1
print (cnt_w)
print (cnt_h)

# 表示して[ESC]が押されるまで待つ
cv2.imshow("image", image)
while cv2.waitKey(33) != 27:
	pass
