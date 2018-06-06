import os
import crypt
import commands
import sys
choice=raw_input("what you want to do \n")
choice=int(choice)
def t1():
	uname=raw_input("Select Username ")
    	upass=raw_input("Select Password ")
	ucrypt=crypt.crypt(upass,"123")
    	os.system("useradd -m -p "+str(ucrypt)+" "+uname)
def t2():
	uname=raw_input("delete Username ")
    	os.system("deluser"+" "+uname)
def t3():
	dirname=raw_input("enter dir. name ")
	os.system("mkdir"+" "+dirname)
def t4():
	dirname=raw_input("enter file name ")
	os.system("chmod g+w"+" "+dirname)

if choice == 1:
	t1()
elif choice == 2:
	t2()
elif choice == 3:
	t3()
elif choice == 4:
	t4()

else:
	print("invalid choice")
