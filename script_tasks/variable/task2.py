import sys
argument= sys.argv
num=int(argument[1])
count=0
while num!=0:
	num=num/10
	count=count+1
if count==1:
	print("number is one digit")
elif count==2:
	print("number is two digit")
else:
	print("number is invalid")
