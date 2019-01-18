# -*- coding: utf-8
from PIL import Image
import numpy as np
import os
import shutil
import sys

def make(dir_name):
	#保存先のディレクトリを作成
	if os.path.isdir("RGB") == False:
		os.mkdir("RGB")
	if os.path.isdir("./RGB/"+dir_name) != False:
		print("そのディレクトリは既に存在します。実行しますか？[y/n]")
		while True:
			choice = input()
			if choice == "y":
				shutil.rmtree("./RGB/"+dir_name)
				os.mkdir("./RGB/"+dir_name)
				os.mkdir("./RGB/"+dir_name+"/rgb")
				os.mkdir("./RGB/"+dir_name+"/r")
				os.mkdir("./RGB/"+dir_name+"/g")
				os.mkdir("./RGB/"+dir_name+"/b")
				break
			elif choice == "n":
				sys.exit("キャンセルしました")
			else:
				continue
	else:
		os.mkdir("./RGB/"+dir_name)

	#処理前の画像のファイル名をリスト化
	return os.listdir(dir_name)

def rgb(f,dir_name):
	img_path = dir_name + "/" + f
	#csvファイルの名前を作成replaceで拡張子を削除
	file_name="./RGB/"+dir_name+"/rgb/"+f.replace(".png","").replace(".jpg","").replace(".gif","").replace(".bmp","")+".csv"
	file_name_r="./RGB/"+dir_name+"/r/"+f.replace(".png","").replace(".jpg","").replace(".gif","").replace(".bmp","")+"_r.csv"
	file_name_g="./RGB/"+dir_name+"/g/"+f.replace(".png","").replace(".jpg","").replace(".gif","").replace(".bmp","")+"_g.csv"
	file_name_b="./RGB/"+dir_name+"/b/"+f.replace(".png","").replace(".jpg","").replace(".gif","").replace(".bmp","")+"_b.csv"
	rgb = Image.open(img_path,"r")
	rgb = rgb.convert("RGB")
	#画像をリサイズ
	rgb = rgb.resize((img_w, img_h))	#(x,y)
	#画像をRGBの配列に変換
	rgb = np.array(rgb)

	data = np.ravel(rgb)
	np.savetxt(file_name, data, fmt="%d,"*1,newline = "", delimiter="")
	fr = open(file_name_r,"a")
	fg = open(file_name_g,"a")
	fb = open(file_name_b,"a")
	for i in range(len(data)):
		if i%3==0:
			if len(data)-i==3:
				fr.write(str(data[i]))
			else:
				fr.write(str(data[i])+",")
		elif i%3==1:
			if len(data)-i==2:
				fg.write(str(data[i]))
			else:
				fg.write(str(data[i])+",")
		elif i%3==2:
			if len(data)-i==1:
				fb.write(str(data[i]))
			else:
				fb.write(str(data[i])+",")
	fr.close()
	fg.close()
	fb.close()

if __name__ == '__main__':
	#画像のサイズの指定（リサイズ）
	print("x,yを100~500の範囲で指定してください")
	print("x=",end="")
	while True:
		img_w = int(input())
		if img_w < 100 or img_w > 500:
			continue
		elif img_w >= 100 and img_w <= 500:
			break
	print("y=",end="")
	while True:
		img_h = int(input())
		if img_h < 90 or img_h > 500:
			continue
		elif img_h >= 90 and img_h <= 500:
			break
	#img_w = 160
	#img_h = 120

	while True:
		#RGB変換を行うディレクトリを選択
		print("ディレクトリ名を入力してください(nで中断)")
		while True:
			dir_name = input()
			if dir_name == "":
				continue
			elif dir_name == "n":
				sys.exit("中断しました")
			else:
				break
		if os.path.isdir(dir_name) == False:
			print("ディレクトリが存在しません\n")
			continue
		img = make(dir_name)

		#csvファイルの作成
		print("csvファイルの作成を開始します")
		i=0
		for f in img:
			rgb(f,dir_name)
			i+=1
			print(str(i)+"/"+str(len(img)))

		print("全ての処理が完了しました")
		print("同じ設定(x="+str(img_w)+",y="+str(img_h)+")で他のディレクトリの画像も変換しますか？[y/n]")
		while True:
			choice = input()
			if choice == "y":
				break
			elif choice == "n":
				sys.exit("終了します")
			else:
				continue
