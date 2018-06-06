#!/user/bin/env python
number=raw_input("enter number of line \n")
choice=raw_input("enter pattern choice \n")
num=int(number)
def pa1(num):
	for i in range(0, num):
			for j in range(0, i+1):
				print ("* ".end="")	
			print("\r")
def pa2(num):
	k=0
	for i in range(0, num):
			numb=num-k
			for j in range(0, numb):
				print ("* ",end="")
			k=k+1	
	  		print("\r")
def pa3(num):
	k = num - 1
	for i in range(0, num):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			print("* ", end="")
		print("\r")
if int(choice)==1:
	pa1(num)
elif int(choice) == 2:
	pa2(num)
		
elif int(choice) == 3:
	pa3(num)
else:
	print("invalid choice")
