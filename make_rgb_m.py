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
	file_name="./RGB/"+dir_name+"/"+f.replace(".png","").replace(".jpg","").replace(".gif","").replace(".bmp","")+".csv"
	rgb = Image.open(img_path,"r")
	rgb = rgb.convert("RGB")
	#画像をリサイズ
	rgb = rgb.resize((img_w, img_h))	#(x,y)
	#画像をRGBの配列に変換
	rgb = np.array(rgb)

	data = np.ravel(rgb)
	temp = np.reshape(data,(img_h,img_w*3))
	np.savetxt(file_name, temp,delimiter=",",fmt='%.0f')

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
