#Kumpulan dari tool tool youtube
#Python 3.7

#LIST PACKAGE
from __future__ import unicode_literals
import youtube_dl
import pytube
import os,time
import random
import sys

#MAIN MENU
print("Menu :")
print("[01] Youtube Mp4 Video Downloader")
print("[02] Audio Mp3 Youtube Downloader")
print("[00] Keluar")
time.sleep(1)

menu = input("Pilihan : ")
#DOWNLOAD VIDEO YOUTUBE DENGAN PACAKGE PYTUBE
if menu == '1' or menu == '01':
	print("Contoh : https://www.youtube.com/watch?v=AdBnKSqGAVA")
	video_link = input('\033[94m Masukan Link Video : ')
	print("[+] Sabar Boz Video na Lagi di Download")
	print("[+] Downloading")
	yt = pytube.YouTube(video_link)
	videos = yt.streams.first()
	videos.download('Hasil')
	print("[!] Video telah di Download")
	print("[!] File saved in YT-Tools/Hasil")
#DOWNLOAD AUDIO YOUTUBE DENGAN PACKAGE YOUTUBE_DL
if menu == '2' or menu == '02':
	video_link = input('\033[94m Masukan Link Video : ')
	ydl_opts = {
		'format' : 'bestaudio/best',
		'postprocessors': [{
			'key' : 'FFmpegExtractAudio',
			'preferredquality': '192'
		}],
		'postprocessors_args': [
			'-ar', '16000'
		],
		'info_dict': [{
			'ext': 'mp3'
		}],
		'prefer_ffmpeg': True,
		'keepvideo': True
	}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([video_link])
		print("[!] telah didownload")

if menu == '0' or menu == '00':
	print("[!] Terimakasih sudah menggunakan tools ini")
	print("[!] Tetap santuy.")
	time.sleep(1)
	print("[!] Mengeluarkan...")
	sys.exit

else :
	if KeyboardInterrupt :
		print("[!] Input Salah")
		sys.exit("[!] Mengeluarkan...")
