#print longest words
f=open('C:/Users/hp/PycharmProjects/untitled2/calc.txt','r')
data=f.read().split()
lw=max(data,key=len)
print(lw)
f.close()