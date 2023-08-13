print('******************* STRING ****************')
nam=('SathisH')
nam1=('KUMAR')
print(type(nam))
print(len(nam))
print(nam[2])
print(nam[0:3])
print(nam[-3])
print(nam[::-1])
print('hello'+' '+nam+' '+'how are you')
print('sathish\nkumar')
print('sathish\t sathish')
print("'sathish'")
print('sathish'r'\new')
print(nam+nam1)
print(nam,nam1)
print('************ STRING FUNCTION ****************')
nam2='sridevi'
nam3=('this my dog')
print(nam2.upper())
print(nam2.lower())
print(nam2.find('i'))
print(nam2.isalpha())
print(nam2.index('dev'))
x=nam2.replace('sridevi','sai')
print('hello',x)
print(nam3.title())
n1='sathish'
n2='kumar'

print(n1,n2)                                            #using , operator
print(n1+n2)                                            #using + operator
print('{} {}'.format('one','two'))                      #using formate operator
print('this is {} and this is {}'.format(n1,n2))        #using formate  operator
print('%s %s'% (n1,n2))                                 #using %(model) operator
print("".join([n1,n2]))                                  #using joint operator
print('********************** NUMBER TYPE *************')
num=255
num1=25.000
num2=25j
print(type(num))
print(type(num1))
print(type(num2))
print(int(num1))
print(float(num))
print(complex(num1))
print(35E3) #scientific number
print('******************* LIST ******************')
L=['sathish','ani','chinna',1,2,3,4,5]
print(type(L))
print(len(L))
print(L[0:3])
print(L[0:])
print(L[3:])
print(L[4])
L[1]='ram' # replacement
L.append('ok')
L.insert(3,'oso')
print(L)
print(L)
del L[3]
print(L)
L.remove(2) # it is not index this is value
print(L)
L.remove('ram')
print(L)
L.pop(0)      #The pop() method like del deletes value at a particular index. But pop() method returns deleted value from the list.
print(L)
k=['a','b','c','d']
k[1:3]=['oo','dd']
k[1:2]=['ok','no']
k=[1:3]=['mmmm]
         

L1=['sai','ani','chinna','dhina']
L1.sort()
print(L1)
L1.reverse()
print(L1)

print('*************************** TUPLE **************')
T=(1)
print(type(T))
t=('1')
print(type(t))
T1=(1,2,3,4,'sai','saran')
print(type(T1))
print(T1)
print('********************DICTIONARY**************')
D={'01':'sathish','02':'sai','03':'kumar','05':'sridevi',6:'sasi','A':'chinna'}
print(type(D))
print(len(D))
print(D.keys())
print(D.values())
print(D['01'])
D['01']='SASASA'
print(D)
del D[6]
print(D)
D.pop('A')
print(D)
#append and remove we  cont ues in dictionary

print('******************* SET *****************')
s={1,2,3,1,1,4,5,'09',10,'a15','sai','ani'}
print(s)
print(type(s))
print(len(s))
s.remove('a15')
print(s)
s.add('sathish')
print(s)
s.pop(3)

# append and del we can't use because this is un order













