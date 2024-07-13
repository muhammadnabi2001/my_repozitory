import os
os.system("clear")
f=open("raqamlar.txt","wt+")

for x in range(1,11):
	f.write(str(x)+" ")
f.seek(0,0)
lis=f.read().split()
sum=0
for y in lis:
	sum +=int(y)
print(sum)
