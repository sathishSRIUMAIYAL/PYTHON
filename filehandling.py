import os
''' read file '''

p=open('myfile.txt' , 'r')
print(p.readline())
print(p.readline())
p.close()

''' file write and create '''

w=open('myfile.txt', 'a')
w.write('oooooooooooooooooooooooooooo')

f=open('myfile.txt','r')
print(f.read())


''' over write'''

p=open('myfile.txt', 'w')
o=p.write('ppppopopopppopo[popppop')

f=open('myfile.txt','r')
y=f.read()


# os.remove('myfile.txt')

# os.rmdir('myfile.txt')