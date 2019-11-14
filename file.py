#append text to a file and display the text

f=open('C:/Users/hp/PycharmProjects/untitled2/calc.txt','a+')
f.seek(0)
f.write('\nkanha')
f.close()
f=open('C:/Users/hp/PycharmProjects/untitled2/calc.txt','r')
data=f.read()
print(data)
f.close()