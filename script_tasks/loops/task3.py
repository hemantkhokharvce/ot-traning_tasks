#!/user/bin/python
import sys
argument= sys.argv
print argument
	for x in range(1, 11):
		print argument[1],"*",x,"=",int(argument[1])*x
