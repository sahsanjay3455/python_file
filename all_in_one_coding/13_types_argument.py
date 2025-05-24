# types of arguments:
# argument is the variable or parameters we used to pass through the function
# def fname(a, b):
#     print(a + b)


# fname(10, 20)
"""
#types of arguments
1.positional args:
i.it is present at function declaration
ii. it is manndatory to pass values
iii.have to take care of position
eg
def add(a,b):<---- positional agrs
    print(a+b)

add(a,b)


2.defult args
i. present at function declaration
ii.its not mandatory to pass values
def  sam(a,b,c=0):
    print(a+b+c)

sam(10,20,30)
sam(10,20) defult arguments

3.keyword args
i.present at fuction calling
ii. it is mandatory to pass values
iii. position is not mandatory
iv.mentio in  the form of k=v (key should follow identifier rules)
eg.
def sam(a,b,c):
    print(a,b,c)
    
sam(a=10,b=20,c=30)
sam(c=30,b=20,a=10) no need or worry about position

4. variable length args
i=present in function declaration
ii. accepts 0 to n numbers of values
note : *a=packing or store as tuples  or accepts as tuples
       **a= it accepts as form of dictionary

def sam(*a):
    print(a)
    
    
sam(100,200,5,6,20,80,88)
sam()
note : *a=packing or store as tuples  or accepts as tuples
       **a= it accepts as form of dictionary
       
       
       
       def sam(*a,**b):
    print(a)
    print(b)
    
sam(100,200,5,6,20,80,88,x=10,y=20,z=30) note: first positional args and keywords arguments


"""


def sam(*a,**b):
    print(a)
    print(b)
    
sam(100,200,5,6,20,80,88,x=10,y=20,z=30)
