#read last n lines of a file

f=open('C:/Users/hp/PycharmProjects/untitled2/calc.txt','r')
data=f.readlines()
print(data[-1])
f.close()

