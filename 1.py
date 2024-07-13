import os
os.system("clear")
f=open("raqamlar.txt","wt+")

for x in range(1,11):
	f.write(str(x)+" ")
f.seek(0,0)
lis=f.read()
print(lis)
