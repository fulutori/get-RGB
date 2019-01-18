# -*- coding: utf-8
from PIL import Image
import numpy as np
import os
import shutil
import sys

def make(dir_name):
	#保存先のディレクトリを作成
	if os.path.isdir(dir_name+"_rgb") != False:
		print("そのディレクトリは既に存在します。実行しますか？[y/n]")
		while True:
			choice = input()
			if choice == "y":
				shutil.rmtree(dir_name+"_rgb")
				os.mkdir(dir_name+"_rgb")
				break
			elif choice == "n":
				sys.exit("キャンセルしました")
			else:
				continue
	else:
		os.mkdir(dir_name+"_rgb")

	#処理前の画像のファイル名をリスト化
	return os.listdir(dir_name)

def rgb(f,dir_name):
	img_path = dir_name + "/" + f
	rgb = Image.open(img_path,"r")
	rgb = rgb.convert("RGB")
	#画像をリサイズ
	rgb = rgb.resize((img_w, img_h))	#(x,y)
	#画像をRGBの配列に変換
	rgb = np.array(rgb,dtype=int)

	#「temp」ディレクトリを作成
	if os.path.isdir("temp") != False:
		shutil.rmtree("temp")
		os.mkdir("temp")
	else:
		os.mkdir("temp")
	#RGB変換した画像の配列の1行目からimg_h行目までのcsvファイルを作成
	for i in range(img_h):
		csv_name = "./temp/" + str(i)
		np.savetxt(csv_name, rgb[i], fmt="%d,"*1,newline = "", delimiter="")

	#「temp」ディレクトリにあるファイルのリストを作成
	csv_file = os.listdir("./temp")
	#「csv_file」をソート（昇順）
	csv_file.sort(key=int)
	#csvファイルの名前を作成replaceで拡張子を削除
	file_name=dir_name+"_rgb/"+f.replace(".png","").replace(".jpg","").replace(".gif","").replace(".bmp","")+".csv"
	if os.path.isfile(file_name) != False:
		os.remove(file_name)
		f = open(file_name,"a")
	else:
		f = open(file_name,"a")
	#「temp」ディレクトリにあるファイルを1つずつ開いて1つのcsvファイルに書き足していく
	for k in csv_file:
		csv_temp = "./temp/"+str(k)
		csv_data = open(csv_temp)
		csv_line = csv_data.readline()
		#f.write(csv_line[:-1]+",") #１行
		f.write(csv_line[:-1]+"\n") #複数行
	f.close()
	#「temp」ディレクトリを削除
	shutil.rmtree("temp")

if __name__ == '__main__':
	#画像のサイズの指定（リサイズ）
	print("x,yを100~1000の範囲で指定してください")
	print("x=",end="")
	while True:
		img_w = int(input())
		if img_w < 100 or img_w > 1000:
			continue
		elif img_w >= 100 and img_w <= 1000:
			break
	print("y=",end="")
	while True:
		img_h = int(input())
		if img_h < 100 or img_h > 1000:
			continue
		elif img_h >= 100 and img_h <= 1000:
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
