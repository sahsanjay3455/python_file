'''
*polymorphism:
poly-->many
morphs--->forms
consider on operator and method (like +,- )
-->definition: it is the process of making the two methods with same name to behave in two different ways
eg + operator ---> svd(sum),mvd(concatenation)

types of polymorphism
1.method overriding (run time polymorphims):
if we have two methods with same name , previous method overrided with the latest method
*method overloading is not possible in python if you try to do method overloading it will act like method overloading

eg:1
def add(a,b):
    print(a+b)

prev=add #monkey patching:  
def add(a,b,c,d,e):
    print(a+b+c+d+e)
    
add(10,30,60,30,50)
prev(10,20)#error: remove the error we need to store address the in one variable call monkey patching 

eg:2
class A:
    def add(self,a,b):
        print(a+b)
    
class B(A):
    def add(self,a,b,c,d):
        print(a+b+c+d)
        
        
ob1=A()
ob2=B()
ob1.add(10,20)
ob2.add(10,20,30,40)


2.operator overloading(compile time polymorphims):
it is the process of making the operators to work  on objects of user defined class by invoking repesctive magic method
eg:magic methods are  :  __add___,__sub__


class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    
    def __sub__(self,other):
        return self.a-other.a
    
    def __mul__(self,other):
        return self.a*other.a
    
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    
    def __mod__(self,other):
        return self.a%other.a
    
    def __pow__(self,other):
        return self.a**other.a
        
        
        
        
        
        
obj1=A(101)
obj2=A(2)
# print(obj1+obj2) #error to remove the error we need magic method
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1//obj2)
print(obj1%obj2)
print(obj1**obj2)

'''

class A:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
    
    def __sub__(self,other):
        return self.a-other.a
    
    def __mul__(self,other):
        return self.a*other.a
    
    def __truediv__(self,other):
        return self.a/other.a
    def __floordiv__(self,other):
        return self.a//other.a
    
    def __mod__(self,other):
        return self.a%other.a
    
    def __pow__(self,other):
        return self.a**other.a
        
        
        
        
        
        
obj1=A(101)
obj2=A(2)
# print(obj1+obj2) #error to remove the error we need magic method
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)
print(obj1/obj2)
print(obj1//obj2)
print(obj1%obj2)
print(obj1**obj2)





