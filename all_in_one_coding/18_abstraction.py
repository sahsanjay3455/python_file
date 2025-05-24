'''
Abstraction: it the process of  hiding implementation   from user by providing only functionality
1.abstract method:it contains only function declaration but not definition
eg:
@abstractmethod
def method_name():
    pass


2.abstract class:
i.if a class contain atleast one abstractmethod it is known as abstract class
ii.for abstract class we can't create objects

class Cname:
    @abstractmethod
    def method_name():
        pass

3.concrete class:
it is the normal class without abstract class
we can create the object of this class


#general syntax for abstraction
from abc import ABC,abstractmethod  #abc-->abstract base class

class abs_class(ABC):
    @abstractmethod
    def method_name():
         pass
     
    @abstractmethod
    def method_name():
        pass
    
class concrete_class(abs_class):
    -----------
    s.b
    --------

'''
# from abc import ABC,abstractmethod
# class ATM_Arch(ABC):
#     @abstractmethod
#     def check_bal():
#         pass

#     @abstractmethod
#     def deposit():
#         pass

#     @abstractmethod
#     def withdraw():
#         pass
# class SBI_ATM(ATM_Arch):
#     def __init__(self,name,pin):
#         self.name=name
#         self.pin=pin
#         self.bal=0
#     @staticmethod
#     def get_pin():
#         return int(input('Enter 4 digit pin: '))
#     def check_bal(self):
#        pin=self.get_pin()
#        if pin==self.pin:
#         print(f'Avl Balance: {self.bal} Rs.')
#        else:
#             print('Incorrect pin')
#     def deposit(self):
#         pin=self.get_pin()
#         if pin==self.pin:
#             amt=int(input('Enter amount: '))
#             self.bal+=amt
#             print(f'Amount of {amt} Rs. deposited.. ✅')
#         else:
#             print('Incorrect pin ❌')
#     def withdraw(self):
#         pin=self.get_pin()
#         if pin==self.pin:
#             amt=int(input('Enter amt: '))
#             if amt<=self.bal:
#                 self.bal-=amt
#                 print(f'Amount of {amt} Rs. got debited ✅')
#             else:
#                 print('Insufficeint funds 😔')
#         else:
#             print('Incorrect pin ❌')

# ob=SBI_ATM('Kiit',1234)