#Kumpulan dari tool tool youtube
#Python 3.7

#LIST PACKAGE
from __future__ import unicode_literals
import youtube_dl
import pytube
import os,time
import random
import sys


#Efek typewriter
def type(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def tyck(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

#Pemilihan OS (Ga Ada gunanya sih:v)
print("Operating system list : ")
print('1. Linux')
print('2. Windows')
time.sleep(1)
OS = input("Pilih Operating system anda : ")
time.sleep(1)

if OS == '1' or OS == 'Linux' or OS == 'linux' :
	os.system("clear")
if OS == '2' or OS ==  'Windows' or OS == 'windows' :
	os.system("cls")
else :
	print("[!] Input Salah")
	sys.exit("[!] Mengeluarkan...")
#Banner ASCII ART
type("██╗   ██╗████████╗████████╗ ██████╗  ██████╗ ██╗     ███████╗")
type("╚██╗ ██╔╝╚══██╔══╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝")
type(" ╚████╔╝    ██║█████╗██║   ██║   ██║██║   ██║██║     ███████╗")
type("  ╚██╔╝     ██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║")
type("   ██║      ██║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║ By")
type("   ╚═╝      ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝  9E(IQZpesial)")

#MAIN MENU
print("Menu :")
print("[01] Youtube Video Downloader")
print("[02] Audio Youtube Downloader")
print("[09] About")
print("[00] Keluar")
time.sleep(1)

menu = input("Pilihan : ")
#DOWNLOAD VIDEO YOUTUBE DENGAN PACAKGE PYTUBE
if menu == '1' or menu == '01':
	print("Contoh : https://www.youtube.com/watch?v=AdBnKSqGAVA")
	video_link = input('\033[94m Masukan Link Video : ')
	tyck("[+] Sabar Boz Video na Lagi di Download")
	tyck("[+] Downloading")
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

#tentang kami kelas 9e
if menu == '9' or menu == '09':
	tyck("	[<3] SEBUAH SHORTCUT TOOLS YOUTUBE [<3]")
	tyck("	[<3]  DENGAN MENGGUNAKAN PYTHON 3  [<3]")

	print("[+] Package yang digunakan : ")
	print("[1] pytube")
	print("[2] youtube_dl")
	time.sleep(1)
	print("")
	print("[+] Team Xzrcty : ")
	print("[1] HydraXZone")
	print("[2] IDKQWEAS")
	print("[3] IQZpesial")
	time.sleep(1)
	print("")
	print("[?] Find this script in https://github.com/qxzcerty")
	print("[?] Ga ada Copyright, 9E Z/SpensA , est 2k19")

if menu == '0' or menu == '00':
	tyck("[!] Terimakasih sudah menggunakan tools ini")
	tyck("[!] Tetap santuy.")
	time.sleep(1)
	print("[!] Mengeluarkan...")
	sys.exit

else :
	if KeyboardInterrupt :
		print("[!] Input Salah")
		sys.exit("[!] Mengeluarkan...")