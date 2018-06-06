#!/user/bin/env python
number=raw_input("enter number of line \n")
choice=raw_input("enter pattern choice \n")
num=int(number)
def pa1(num):
	       i=0
	       while i<=num:
			j=0
			while j <= i:
				print("* ",end"")
				j += 1
			i+=1	
			print("\n")
def pa2(num):
	       i=0
	       while i<=num:
			num -= 1
			j=0
			while j <= num:
				print("* ",end"")
				j+=1	
	  		print("\n")
def pa3(num):
	i=0	
	k = num - 1
	while i<num:
		j=0
		l=0
		while l<k:
			print(" ",end"")
			l=l+1
		k = k - 1
		while j <= i:
			print("* ",end"")
			j=j+1
		print("\r")
		i=i+1
if int(choice)==1:
	pa1(num)
elif int(choice) == 2:
	pa2(num)
		
elif int(choice) == 3:
	pa3(num)
else:
	print("invalid choice")
