import os
import os.path
from getpass import getpass
os.system("clear")
def banner():
	print("\033[1;36;40m_                                   _                _")
	print("| |_ ___ _ __ _ __ ___  _   ___  __ | |__   __ _  ___| | _____ _ __")
	print("| __/ _ \ '__| '_ ` _ \| | | \ \/ / | '_ \ / _` |/ __| |/ / _ \ '__|")
	print("| ||  __/ |  | | | | | | |_| |>  <  | | | | (_| | (__|   <  __/ |")
	print(" \__\___|_|  |_| |_| |_|\__,_/_/\_\ |_| |_|\__,_|\___|_|\_\___|_|\033[0m")
	print("                \033[1;34;40m author by \033[1;33;40mTechnical Dangwal\033[0m")
	print("")
banner()
if not os.path.exists("/data/data/com.termux/files/usr/share/user.txt"):
	f=open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
	f.write("cd Login ; python login.py")
	f.close()
	user=input("\033[1;33;40mSET YOUR USERNAME :\033[0m")
	print("")                                                        
	print("")
	print("")
	print("")
	passwd=getpass("\033[1;33;40mSET YOUR PASSWORD :\033[0m")
	f=open("/data/data/com.termux/files/usr/share/user.txt","w")                                            
	f.write(f"{user}\n")
	f.write(passwd)                                           
	f.close()
else:
	while(1):
		try:
			f=open("/data/data/com.termux/files/usr/share/user.txt","r")
			username=f.readline()
			username=username.strip()
			password=f.readline()
			password=password.strip()
			f.close()
			usr=input("\033[1;33;40mEnter username -: \033[0m")
			if usr==username:
				pas=getpass("\033[1;33;40mEnter password -: \033[0m")
				if pas==password:
					os.system("clear")
					banner()
					break
				else :
					print("")
					print("")
					print("")
					print("")
					print("\033[1;31;40m try again\033[0m")
					print("")
					print("")
					print("")
					print("")
			else:
				print("")
				print("")
				print("")
				print("")
				print("")
				print("\033[1;31;40m try again\033[0m")
				print("")
				print("")
				print("")
				print("")
		except KeyboardInterrupt as e:
			print("")
			print("")
			print("")
			print("")
			print("\033[1;31;40m",e,"\033[0m")
			print("")
			print("")
			print("")
			print("")
