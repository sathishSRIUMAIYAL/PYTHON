

print('************************FOR LOOP*******************************')
nam='sathish'
a=0
for i in nam:
    print(nam[0:a])
    a+=1
for i in nam:
    print(nam[0:a])
    a-=1
print('********************************************************************')
for i in range(11):
    print(f'number{i}')
print('********************************************************************')
for i in 'sathishkumar':
    if i=='s' or i=='a':
        continue
    print('letter',i)
print('********************************************************************')
li=['sathish','kumar','sai']
for i in range(len(li)):
    print(li[i])
print('********************************************************************')
for i in range(5):
    for j in range(i+1):
        print('$',end=' ')
    for j in range(i,4):
        print(' ',end=' ')
    for j in range(i,4):
        print(' ',end=' ')
    for j in range(i+1):
        print('$',end=' ')

    print(' ')





print('*********************WHILE LOOP**********************************')
lat=' '
while not lat.isalpha():
    lat=input('enter your name:')
    print(lat)
print('*******************************************************')
num=0
while True:
    num+=1
    print(f'countis{num}')
    if num==10:
        break
print('*******************************************************')
c=0
while c<5:
    c+=1
    print(c)
print('*******************************************************')
s='sathishkumar'
i=0
while i<(len(s)):
    if s[i]=='s':
        i+=1
        continue
    print('latter',s[i])
    i+=1
print('*******************************************************')
import random
num=random.randint(1,20)
guess=int(input('enter your name'))
while guess!=num:
    if guess>num:
        print('this number is height try again')
    elif guess<num:
        print('this number is low try again')
    guess = int(input('enter your name'))
else:
    print('you won')

print('***********************END********************************')


