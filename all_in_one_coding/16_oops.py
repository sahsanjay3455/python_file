# object oriented programming
# clas,object , types of properties/states,contructor,types of method,inheritance,polymorphism,encapsulation , abstraction

# why oops is importants
"""
l=['yash',401,95,'swaroop',402,85,'adnan',403,79,'pavini',404,99]
i.data is not properly organized data
so to organized the data we need oops
inheritance-- code reusability
polymorphism--- multi behaviour nature
encapsulation --- data security
abstraction ----- data hiding



#class: it is the blues print which is used to store properties and fuctionalities of an object
#object: it the real world entity  or instance(exact copy) of the class
eg
degree certificate(original ---> class)



#syntax

class Cname:(pascal)
------------
properties
functionalities
-------------
obj_name=Cname(args)
here arguments are optional to pass






# q
class demo:
    a = 10
    b = 20
    # def fname():#this is method but outside fun callled function


obj1 = demo()
obj2 = demo()
obj3 = demo()
# accessing the properties
# i. cname.propertyname
# ii. object_name.propertyname
print(demo.a, demo.b)
print(obj1.a,obj2.b)
print(obj2.a,obj2.b)
#modifying the
#cname.propertyname=new_value
#obj_nmae.propertyname=new_value

"""


# class bank:
#     bname = "sbi"
#     ifsc = "sbi007"
#     loc = "bhubneshwar"


# c1 = bank()
# c2 = bank()
# print("Bank:", bank.bname, bank.ifsc, bank.loc)
# print("Bank:", c1.bname, c1.ifsc, c1.loc)
# print("Bank:", c2.bname, c2.ifsc, c2.loc)
# if we try to modify the properties by using class name then it will modify in all the other objects
# bank.loc = "banglore"
# print("Bank:", bank.bname, bank.ifsc, bank.loc)
# print("Bank:", c1.bname, c1.ifsc, c1.loc)
# print("Bank:", c2.bname, c2.ifsc, c2.loc)

# if we try to modify the properties by using object name then it wiil modify in that specific object only
# print('\n')
# c2.loc='birgunj'
# print("Bank:", bank.bname, bank.ifsc, bank.loc)
# print("Bank:", c1.bname, c1.ifsc, c1.loc)
# print("Bank:", c2.bname, c2.ifsc, c2.loc)


# q1 create class school with some properties and try with accessing  and modification


# class School:
#     sname = "ghp school"
#     board = "SEE"
#     loc = "birgunj"


# obj1 = School()
# obj2 = School()
# print(School.sname, School.board, School.loc)
# print(obj1.sname, obj1.board, obj1.loc)
# print(obj2.sname, obj2.board, obj2.loc)
# modifying on class name
# print('\n')
# School.loc = "ktm"
# print(School.sname, School.board, School.loc)
# print(obj1.sname, obj1.board, obj1.loc)
# print(obj2.sname, obj2.board, obj2.loc)
# modifying on object name
# print('\n')
# obj2.loc = "ktm"
# print(School.sname, School.board, School.loc)
# print(obj1.sname, obj1.board, obj1.loc)
# print(obj2.sname, obj2.board, obj2.loc)


"""
types of states/properties
1.class memeber:class memebers are common for all the objects
eg: bank: bname,bloc,bcontact, bemail

2. object member:these members are different for all the object
eg: bank: customer name,acno,bank balance,phoneno,address, aadhar no etc

"""
# class Bank:
#     name='SBI'
#     ifsc='SBI00089'
#     loc='Hyderabad'

# c1=Bank()
# c2=Bank()
# c3=Bank()
# object members
# c1.name='pavini'
# c1.acno=34567

# c2.name='sanjay'
# c2.acno=3456

# c3.name='ram'
# c3.acno=4567

# print(a1.na)

"""
constructor:(__init__) -->initialization method
1.it is a method which is  used to initialize the object members
2. __init__ is a self invoking method()--- no need to call-- at the time of object creation it will get called automatically
3. it is mandatory to use self as an argument and it should be 1st argument
4. self is used to store object address automatically
5.according to convention it is compulsory to use self as argument

syntax:
class Cname:
    def __init__(self,arg1,arg2,...,argn):
        self.arg1=arg1
        self.arg2=arg2
        ......
        ......
        self.agrn=argn
"""
# eg:
# class Bank:
#     name='SBI'
#     ifsc='SBI00089'
#     loc='Hyderabad'
#     def __init__(self,name,acno):
#         self.name=name
#         self.acno=acno


# print(Bank.name,Bank.ifsc,Bank.loc)
# c1=Bank('sanjay',456789)
# c2=Bank('yash',3456789)
# c3=Bank('suyash',345678)
# print(c1.name,c1.acno)
# print(c2.name,c2.acno)
# print(c3.name,c3.acno)
# print(c3.name,c3.ifsc,c3.loc)

# class Zoo:
#     name = 'xyz zoo'
#     loc = 'hyderabad'
#     contact = 34567567
#     email = 'xyz123@gmail.com'

#     def __init__(self, animal_name, gender, age, health_status):  # corrected __init__
#         self.animal_name = animal_name
#         self.gender = gender
#         self.age = age
#         self.health_status = health_status

# # Creating instances
# lion = Zoo('lion', 'male', 18, 'healthy')
# zebra = Zoo('zebra', 'female', 25, 'diseased')
# ape = Zoo('ape', 'male', 30, 'healthy')
# leopard = Zoo('leopard', 'male', 20, 'healthy')

# # Printing details
# print(lion.animal_name, lion.gender, lion.age, lion.health_status)
# print(zebra.animal_name, zebra.gender, zebra.age, zebra.health_status)
# print(ape.animal_name, ape.gender, ape.age, ape.health_status)
# print(leopard.animal_name, leopard.gender, leopard.age, leopard.health_status)


"""
types of methods
i.object method: to access and modify the object members , we will used object method
how to create object method
-- it is mandatory to pass self as 1st argument
self will store object address
syntax:
1.objname.methodname(args)
2.cname.methodname(objname)
eg:
class Bank:
    bname = "SBI"
    loc = "banglore"

    def __init__(self, name, acno):
        self.name = name
        self.acno = acno

    # object method or to access the obj members
    def display(self):
        print("name:", self.name)
        print("acno:", self.acno)
        
    def change_name(self):
        new_name=input('enter name:')
        self.name=new_name


c1 = Bank("sanjay", 56789)
c2 = Bank("bob", 56789)
c3 = Bank("virat", 45678)
c1.display()
c2.display()
c3.display()
print('\n')
print('change the c3 name \n')
c3.change_name()
c3.display()
    

ii.class method:to access and modify the class members , we will use class method
*To create class method it is mandatory to use @classmethod decorator
*it is compulsory to use cls as 1st argument
*cls will store address of class
*cls also work as class name

syntax:
Cname.methodname(args)
obj.methodname(args)
eg:
class Bank:
    bname = "SBI"
    loc = "banglore"

    def __init__(self, name, acno):
        self.name = name
        self.acno = acno

    # object method or to access the obj members
    def display(self):
        print("name:", self.name)
        print("acno:", self.acno)

    def change_name(self):
        new_name = input("enter name:")
        self.name = new_name

    # to access class members
    @classmethod
    def dis(cls):
        print("bank name", cls.bname)
        print("bank location", cls.loc)
        
    #to modify the class members
    @classmethod
    def change_loc(cls,new_loc):
        cls.loc=new_loc


c1 = Bank("sanjay", 56789)
c2 = Bank("bob", 56789)
c3 = Bank("virat", 45678)
# c1.display()
# c2.display()
# c3.display()
# print("\n")
# print("change the c3 name \n")
# c3.change_name()
# c3.display()
# disply class members
Bank.dis()
Bank.change_loc('mumbai')
Bank.dis()
c1.dis()
c2.dis


iii.static method: it is neither related class nor related to object it acts as a supportive method
* it is mandatory to use @staticmethod decorator
*no need to used self or cls arguments
*syntax:
self.methodname(args)-->to access staticmethod inside object method
cls.methodname(args)-->to access staticmethod inside class method
 

class Bank:
    bname = 'SBI'
    loc = 'Banglore'

    def __init__(self, name, acno, pin):  # ✅ corrected here
        self.name = name
        self.acno = acno
        self.bal = 0
        self.pin = pin

    # Object method to access object members
    def display(self):
        print('Name: ', self.name)
        print('Acno: ', self.acno)

    # Modify object members
    def change_name(self):
        new_name = input('Enter name: ')
        self.name = new_name

    # Access class members
    @classmethod
    def disp(cls):
        print('Bank name: ', cls.bname)
        print('Bank loc: ', cls.loc)

    # Modify class members
    @classmethod
    def change_loc(cls, new):
        cls.loc = new

    @staticmethod
    def add(bal, amt):
        return bal + amt

    @staticmethod
    def get_pin():
        pin = int(input('Enter 4-digit pin: '))
        return pin

    def check_bal(self):
        pin = self.get_pin()
        if pin == self.pin:
            print('Account bal is: ', self.bal, 'Rs.')
        else:
            print('Incorrect pin')

    def deposit(self):
        pin = self.get_pin()
        if pin == self.pin:
            amt = int(input('Enter amount to deposit: '))
            self.bal = self.add(self.bal, amt)
            print(f'Amount of {amt} Rs deposited successfully')
        else:
            print('Incorrect pin')

    @staticmethod
    def sub(bal, amt):
        if bal >= amt:
            return bal - amt
        else:
            print('Balance is not sufficient')
            return bal  

    def withdraw(self):
        pin = self.get_pin()
        if pin == self.pin:
            amt = int(input('Enter amount to withdraw: '))
            self.bal = self.sub(self.bal, amt)
        else:
            print('Incorrect pin')

# Creating customers
c1 = Bank('Taj Shaik', 9087889786778, 1234)
c2 = Bank('Bob', 9087999786778, 7890)
c3 = Bank('Virat', 3487999786778, 9090)

# Sample transaction
c1.check_bal()
c1.deposit()
c1.check_bal()
c1.withdraw()
c1.check_bal()



"""


# class Bank:
#     bname = "SBI"
#     loc = "banglore"

#     def __init__(self, name, acno,pin):
#         self.name = name
#         self.acno = acno
#         self.bal=0
#         self.pin=pin

#     # object method or to access the obj members
#     def display(self):
#         print("name:", self.name)
#         print("acno:", self.acno)

#     def change_name(self):
#         new_name = input("enter name:")
#         self.name = new_name

#     # to access class members
#     @classmethod
#     def dis(cls):
#         print("bank name", cls.bname)
#         print("bank location", cls.loc)

#     #to modify the class members
#     @classmethod
#     def change_loc(cls,new_loc):
#         cls.loc=new_loc

#     def check_bal(self):
#         pin=int(input('enter 4 digits pin:'))
#         if pin==self.pin:
#             print('account bal is:',self.bal)
#         else:
#             print('incorrect pin')
#     @staticmethod
#     def add(bal,amt):
#         return (bal+amt)

#     def deposite(self):
#          pin=int(input('enter 4 digits pin:'))
#          if pin==self.pin:
#             amt=int(input('enter a amount:'))
#             self.bal=self.add(self.bal,self.amt)
#          else:
#              print('pin is incorrect')


# c1 = Bank("sanjay", 56789789,1234)
# c2 = Bank("bob", 567895678,8989)
# c3 = Bank("virat", 4567856789,8989)
# # c1.display()
# # c2.display()
# # c3.display()
# # print("\n")
# # print("change the c3 name \n")
# # c3.change_name()
# # c3.display()
# # disply class members
# # Bank.dis()
# # Bank.change_loc('mumbai')
# # Bank.dis()
# # c1.dis()
# # c2.dis
# c1.check_bal()
# c1.deposite()


# class Bank:
#     bname = 'SBI'
#     loc = 'Banglore'

#     def __init__(self, name, acno, pin):  # ✅ corrected here
#         self.name = name
#         self.acno = acno
#         self.bal = 0
#         self.pin = pin

#     # Object method to access object members
#     def display(self):
#         print('Name: ', self.name)
#         print('Acno: ', self.acno)

#     # Modify object members
#     def change_name(self):
#         new_name = input('Enter name: ')
#         self.name = new_name

#     # Access class members
#     @classmethod
#     def disp(cls):
#         print('Bank name: ', cls.bname)
#         print('Bank loc: ', cls.loc)

#     # Modify class members
#     @classmethod
#     def change_loc(cls, new):
#         cls.loc = new

#     @staticmethod
#     def add(bal, amt):
#         return bal + amt

#     @staticmethod
#     def get_pin():
#         pin = int(input('Enter 4-digit pin: '))
#         return pin

#     def check_bal(self):
#         pin = self.get_pin()
#         if pin == self.pin:
#             print('Account bal is: ', self.bal, 'Rs.')
#         else:
#             print('Incorrect pin')

#     def deposit(self):
#         pin = self.get_pin()
#         if pin == self.pin:
#             amt = int(input('Enter amount to deposit: '))
#             self.bal = self.add(self.bal, amt)
#             print(f'Amount of {amt} Rs deposited successfully')
#         else:
#             print('Incorrect pin')

#     @staticmethod
#     def sub(bal, amt):
#         if bal >= amt:
#             return bal - amt
#         else:
#             print('Balance is not sufficient')
#             return bal

#     def withdraw(self):
#         pin = self.get_pin()
#         if pin == self.pin:
#             amt = int(input('Enter amount to withdraw: '))
#             self.bal = self.sub(self.bal, amt)
#         else:
#             print('Incorrect pin')

# # Creating customers
# c1 = Bank('Taj Shaik', 9087889786778, 1234)
# c2 = Bank('Bob', 9087999786778, 7890)
# c3 = Bank('Virat', 3487999786778, 9090)

# # Sample transaction
# c1.check_bal()
# c1.deposit()
# c1.check_bal()
# c1.withdraw()
# c1.check_bal()


"""
inheritance:
process of deriving the properties from parent class to child class
--flow from top to bottom but reverse is not allow
parent class----->old version of inst 1.pic uploasd 2.message 3.video upload
    |
    | Inherit
    |
 child class   ----> new version 1.reels,2.stories
 
 types of inheritace:
 1.single level inheritance:process of deriving the properties from parent class to child class 
 
 class Parent:
    a=10
    b=20
    def __init__(self,c,d):
        self.c=c
        self.d=d

class Child(Parent):
        x=10
        y=20


ob=Child(100,200)
print(ob.a,ob.b,ob.c,ob.d,ob.x,ob.y)

 
  *constructor chaining:
 it is the process of calling constructor of parent class inside the constructor of child 
 #syntax: any one is to remember
 1. super().__init__(args)
 2.super(child,self).__(args)
 3. parent.__init__(self,args)
 *method chainig:
 it is process of calling method of parent class inside the method of child class
  #syntax: any one is to remember
 1. super().methodname(args)
 2.super(child,self/cls).methodname(args)
 3. parent.methodname(self/cls,args)
 
 eg:
 class Bank:
    bname = "SBI"
    loc = "Hyderabad"

    def __init__(self, name, phno):
        self.name = name
        self.phno = phno
    def display(self):
        print("Name", self.name)
        print("phone no:", self.phno)
        

class Bank_new(Bank):
    def __init__(self, name, phno, acno):
        super().__init__(name, phno)
        self.acno = acno

    def display(self):
        super().display()
        print("account no:", self.acno)


c1 = Bank_new("sanjay", 9845040877,345678)
c1.display()
 
 2. multi-level inheritance:
 it is process of deriving the properties from parent class to child class by considering the more level
 class A:
    a=100
    b=200
 
class B(A):
    y=2000
    def __init__(self,c,d):
        self.c=c
        self.d=d
        
class C(B):
    p=120
    q=90
    
ob=C(120,78)
print(ob.a,ob.b,ob.y,ob.c,ob.d,ob.p,ob.q)

 
 3.multiple inheritance:
 process of deriving the properties from mutiple parent classes to a single child class
 eg: priority on A --->class C(A,B) 
 class A:
    a=190
    b=900
    @classmethod
    def display(cls):
        print('from class A')
        print(cls.a,cls.b)
        
class B:
    x=100
    y=200
    @classmethod
    def display(cls):
        print('from class B')
        print(cls.x,cls.y)
        
class C(A,B):
    p=1000
    q=200
    
    
    
ob=C()
print(ob.a,ob.b,ob.x,ob.y,ob.p,ob.q)
ob.display()


OR_____________
 eg: priority on B --->class C(B,A) 
class A:
    a=190
    b=900
    @classmethod
    def display(cls):
        print('from class A')
        print(cls.a,cls.b)
        
class B:
    x=100
    y=200
    @classmethod
    def display(cls):
        print('from class B')
        print(cls.x,cls.y)
        
class C(B,A):
    p=1000
    q=200
    
    
    
ob=C()
print(ob.a,ob.b,ob.x,ob.y,ob.p,ob.q)
ob.display()

 
 4.heirarichal inheritance:
 process of deriving the properties from single parent to multiple child classes
 
 class Restaurant:
    name = "Arabian Restaurant"
    menu = {
        "chicken biriyani": 300,
        "mutton biriyani": 500,
        "paneer curry": 150,
        "coke": 25,
    }

    @classmethod
    def disp_menu(cls):
        print("-----MENU------")
        for i in cls.menu:
            print(i, "     ", cls.menu[i])


class Swiggy(Restaurant):
    def __init__(self, name, phno, addr):
        self.name = name
        self.phno = phno
        self.addr = addr
        self.cart = {}

    def order(self):
        while True:
            Restaurant.disp_menu()
            item = input("Enter your food item: ")
            if item in Restaurant.menu:
                self.cart[item] = Restaurant.menu[item]
                print(f"{item} added to your cart")
            else:
                print(f"sorry we are not delivering {item}")
            choice = input("Do you want to add more? (y/n): ").lower()
            if choice == "y":
                continue
            else:
                break


class Zomato(Restaurant):
    def __init__(self, name, phno, addr):
        self.name = name
        self.phno = phno
        self.addr = addr
        self.cart = {}

    def order(self):
        while True:
            Restaurant.disp_menu()
            item = input("Enter your food item: ")
            if item in Restaurant.menu:
                self.cart[item] = Restaurant.menu[item]
                print(f"{item} added to your cart")
            else:
                print(f"sorry we are not delivering {item}")
            choice = input("Do you want to add more? (y/n): ").lower()
            if choice == "y":
                continue
            else:
                break

    def disp_cart(self):
        print(self.cart)


# ob=Swiggy('KIIT',6778677867,'Bhubaneshwar Kiit college')

ob1 = Zomato("KIIT", 6778677867, "Bhubaneshwar Kiit college")
ob1.order()
ob1.disp_cart()




 
 5.hybrid inheritance :combination of two inheritance:
 it is the combination of more than one inheritance
 
#mutiple-heirarchical
class A:
    a=10
    b=20
    
class B:
    x=100
    y=200
    
class C(A,B):
    s=2000
    t=900
    
class D(C):
    e=300
    f=900
    
class E(C):
    g=90
    h=80
    
ob1=D()
obj2=E()
print(ob1.a,ob1.b,ob1.s,ob1.t,ob1.e,ob1.f,ob1.x,ob1.y)
print(obj2.g,obj2.h)
 
 

 
"""
# class Parent:
#     a=10
#     b=20
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d

# class Child(Parent):
#         x=10
#         y=20


# ob=Child(100,200)
# print(ob.a,ob.b,ob.c,ob.d,ob.x,ob.y)


# class Bank:
#     bname = "SBI"
#     loc = "Hyderabad"

#     def __init__(self, name, phno):
#         self.name = name
#         self.phno = phno
#     def display(self):
#         print("Name", self.name)
#         print("phone no:", self.phno)


# class Bank_new(Bank):
#     def __init__(self, name, phno, acno):
#         super().__init__(name, phno)  #constructor chaining
#         self.acno = acno

#     def display(self):
#         super().display()   #method chaining
#         print("account no:", self.acno)


# c1 = Bank_new("sanjay", 9845040877,345678)
# c1.display()

# class A:
#     a=100
#     b=200

# class B(A)::
#     y=2000
#     def __init__(self,c,d):
#         self.c=c
#         self.d=d

# class C(B):
#     p=120
#     q=90

# #creating the object of child class (C)
# ob=C(120,78)
# print(ob.a,ob.b,ob.y,ob.c,ob.d,ob.p,ob.q)


# multiple inheritance eg:
# class A:
#     a=190
#     b=900
#     @classmethod
#     def display(cls):
#         print('from class A')
#         print(cls.a,cls.b)

# class B:
#     x=100
#     y=200
#     @classmethod
#     def display(cls):
#         print('from class B')
#         print(cls.x,cls.y)

# class C(B,A):
#     p=1000
#     q=200


# ob=C()
# print(ob.a,ob.b,ob.x,ob.y,ob.p,ob.q)
# ob.display()

#heirarichal inheritance

# class Restaurant:
#     name = "Arabian Restaurant"
#     menu = {
#         "chicken biriyani": 300,
#         "mutton biriyani": 500,
#         "paneer curry": 150,
#         "coke": 25,
#     }

#     @classmethod
#     def disp_menu(cls):
#         print("-----MENU------")
#         for i in cls.menu:
#             print(i, "     ", cls.menu[i])


# class Swiggy(Restaurant):
#     def __init__(self, name, phno, addr):
#         self.name = name
#         self.phno = phno
#         self.addr = addr
#         self.cart = {}

#     def order(self):
#         while True:
#             Restaurant.disp_menu()
#             item = input("Enter your food item: ")
#             if item in Restaurant.menu:
#                 self.cart[item] = Restaurant.menu[item]
#                 print(f"{item} added to your cart")
#             else:
#                 print(f"sorry we are not delivering {item}")
#             choice = input("Do you want to add more? (y/n): ").lower()
#             if choice == "y":
#                 continue
#             else:
#                 break


# class Zomato(Restaurant):
#     def __init__(self, name, phno, addr):
#         self.name = name
#         self.phno = phno
#         self.addr = addr
#         self.cart = {}

#     def order(self):
#         while True:
#             Restaurant.disp_menu()
#             item = input("Enter your food item: ")
#             if item in Restaurant.menu:
#                 self.cart[item] = Restaurant.menu[item]
#                 print(f"{item} added to your cart")
#             else:
#                 print(f"sorry we are not delivering {item}")
#             choice = input("Do you want to add more? (y/n): ").lower()
#             if choice == "y":
#                 continue
#             else:
#                 break

#     def disp_cart(self):
#         print(self.cart)


# # ob=Swiggy('KIIT',6778677867,'Bhubaneshwar Kiit college')

# ob1 = Zomato("KIIT", 6778677867, "Bhubaneshwar Kiit college")
# ob1.order()
# ob1.disp_cart()

# class A:
#     a=10
#     b=20
    
# class B(A):
#     x=100
#     y=200
    
# class C(B):
#     p=1000
#     q=2000
    
# class D(B):
#     s=890
#     u=678
    
# obj1=C()
# obj2=D()

# print(obj1.a,obj1.b,obj1.x,obj1.y,obj1.p,obj1.q)
# print(obj2.s,obj2.u)

#mutiple-heirarchical
# class A:
#     a=10
#     b=20
    
# class B:
#     x=100
#     y=200
    
# class C(A,B):
#     s=2000
#     t=900
    
# class D(C):
#     e=300
#     f=900
    
# class E(C):
#     g=90
#     h=80
    
# ob1=D()
# obj2=E()
# print(ob1.a,ob1.b,ob1.s,ob1.t,ob1.e,ob1.f,ob1.x,ob1.y)
# print(obj2.g,obj2.h)