print('*********************** class , object and class variable  *************************')
class Data:
    variable=0                                         # CLASS VARIAPLE

    def __init__(self,username,password,email):
        self.USERNAME=username                        # instance variable
        self.PASSWORD=password
        self.EMAIL=email
        Data.variable+=1

    def username (self):
        print('username:'+self.USERNAME)
    def password (self):
        print('password'+self.PASSWORD)
    def email (self):
        print('email:'+self.EMAIL)



#from opps import Data
user1=Data('sathish','1245246','sathish439')
user2=Data('aarnave','123456','aarnvee@123')

user1.username()
user1.password()
user2.email()

print(Data.variable)

print('**************************************************************************************************************')






print('***************************INHERITS**********************************************************************')

class username_passeord():                                      # parent class , bass class , super class.
    def __init__(self,username,passeord):
        self.USER=username
        self.PW=passeord

    def user_pwz(self):
        print('username',self.USER)
        print('password',self.PW)


class student(username_passeord):                        # student class inherits username_password class  (child class , dervied class , sub class .)

    def __init__(self ,username,password,age,year_of_pasedout):
        self.AGE=age
        self.YOP=year_of_pasedout
        username_passeord.__init__(self,username,password)


    def age_yop(self):
        print(self.USER+'age is',self.AGE )
        print(self.USER+'year of passed out ',self.YOP)



#from refer import *

user=student('sathish',15254439,25,2020)

user.user_pwz()
user.age_yop()


print('***********************************  abstract **********************************************************')
from abc import ABC,abstractmethod
# you cannot creat object for abstract class
# classes inheriting abstract class must override all abstract methds

class polygon (ABC):              # abstract class
    @abstractmethod              #decorator
    def noofsides(self):
        pass


class triangal (polygon):            # concreat class
    def noofsides(self):
        print('your raiding a car....')


class pentadon (polygon):
    def noofsides(self):
        print('your riding bike...')




a1=triangal()
a1.noofsides()

b1=pentadon()
b1.noofsides()









