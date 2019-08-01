import os 
import time
import getpass
def main():
    while(1):
        os.system("clear")
        os.system("figlet Login-pannel |lolcat")
        print("")
        print("")
        print("")
        print("")
        try:
            a=input("Enter username:-")
            if a=="aditya":
                print("wait.........")
                time.sleep(4)
                print("")
                print("")
                print("")
                print("")
            else:
                print("Wrong  username")
                time.sleep(2)
                continue
            b=getpass.getpass("Enter password:-")
            if b=="aditya1234":
                print("wait.......")
                time.sleep(2)
                os.system("clear")
                os.system("figlet "+ a +" |lolcat")
                break
            else:
                print("wrong password")
                continue
        except KeyboardInterrupt:
            print("")
            os.system("killall -9 com.termux")
            print("")
            print("wrong password")
main()  