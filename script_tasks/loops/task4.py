number=raw_input("enter the number\n")
num=int(number)
print("prime numbers are")
for i in range(2, num+1):
	flag=0
	for j in range(2, i):
		if i%j==0:
 			flag=flag+1
	if flag==0 and i!=2:
 		print(i)
print("even numbers are")
for i in range(1, num+1):
	if i%2==0:
		print(i)
print("odd numbers are")
for i in range(1, num+1):
	if i%2!=0:
		print(i)

	 
