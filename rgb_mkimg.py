#coding: utf-8

import numpy as np
import cv2

arr = np.genfromtxt("./DQqMrVnVoAAmcpb.csv", delimiter=",", dtype=np.int32)
cnt=0
rgba_all=[] #RGBAで一区切りにした配列
rgba=[]
for x in arr: #一次元配列をRGBAで一区切りにする
	if cnt==3:
		cnt=0
		rgba=[]
	rgba.append(x)
	cnt+=1
	if len(rgba)==3:
		rgba_all.append(rgba)
"""
i=0
#色の指定
r=103
g=88
b=85
for x in rgba_all: #1pxごとのRGBAを取り出して指定色をカウント
	if (x[0]==r and x[1]==g and x[2]==b): #指定色の場合は加算
		i+=1
print ("(R,G,B)=(%d,%d,%d)は%d個存在します" %(r,g,b,i))
"""
#生成する画像のサイズ
cols = 353
rows = 500

#イメージ生成
image = np.zeros((rows, cols, 3), np.uint8)

cnt_w=0
cnt_h=0
#rgbから画像を生成
for rgba in rgba_all:
	image[cnt_h:cnt_h+1,cnt_w:cnt_w+1] = [int(rgba[2]),int(rgba[1]),int(rgba[0])]
	cnt_w+=1
	if cnt_w!=0 and cnt_w%cols==0:
		cnt_w=0
		cnt_h+=1
print (cnt_w)
print (cnt_h)

# 表示して[ESC]が押されるまで待つ
cv2.imshow("image", image)
while cv2.waitKey(33) != 27:
	pass
