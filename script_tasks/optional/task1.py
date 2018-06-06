import os
import crypt
import commands
import sys
uname=raw_input("Select Username ")
upass=raw_input("Select Password ")
ucrypt=crypt.crypt(upass,"123")
os.system("useradd -m -p "+str(ucrypt)+" "+uname)
