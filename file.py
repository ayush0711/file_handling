# write a python program to read  an entire text file

f=open('C:/Users/hp/PycharmProjects/untitled2/calc.txt','r')
data=f.read()
print(data)
f.close()


#read n no. of lines

f=open('C:/Users/hp/PycharmProjects/untitled2/calc.txt','r')
a=int(input())
for i in range(a):
    a=f.readline()
    print(a)
f.close()