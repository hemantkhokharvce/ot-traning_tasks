import os
import os.path as osp
path=raw_input("enter the path\n")
dirs= os.listdir(path)
print("All Files in the given path :")
for file in dirs: 
	print file
print("Files above 500 bytes :") 
for file in dirs:
	 	size_byte = ((osp.getsize(path + file)))
	 	if size_byte > 500:
			print file + " " + str(size_byte)

html_str = "<html><body><table><tr><th>File name</th><br><th>File path</th><br><th>File size</th><br></tr></table></body></html>"
f = open("page.html","w")
f.write(html_str)
f= open("page.html")
		
	
