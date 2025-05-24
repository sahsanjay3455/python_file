# user define function
# making the calculator
# def add(a, b):
#     print("sum of two num:", a + b)


# def sub(a, b):
#     print("diff of two num:", a - b)


# def mult(a, b):
#     print("multiplicatio is:", a * b)


# def div(a, b):
#     print("division is:", a // b)


# def cal(a, b):
#     add(a, b)
#     sub(a, b)
#     mult(a, b)
#     div(a, b)


# a = int(input("enter first num:"))
# b = int(input("enter second num:"))
# cal(a, b)

# 1.without argument and without return

# Q1. wap to find the factorial of given number

# def factorial():
#     num=int(input('enter a num:'))

#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     print('factorial is:',fact)

# factorial()

# q2.wap to get the following output

# s = '1001001010abc#$%'
# out = '0110110101abc#$%'


# def replacing():
#     output = ''

#     for char in s:
#         if char == '1':
#             output += '0'
#         elif char == '0':
#             output += '1'
#         else:
#             output += char
#     print(output)

# replacing()

# q3. wap to extract only positive integer from a givene list

# l=[10,20,-890,5.6,True,'hello',[1,2,3,4]]
# out=[10,20]

# def extract():
#     output=[]
#     for i in l:
#         if type(i)==int and i>0:
#                 output.append(i)

#     print(output)

# extract()

# 2. function with args and without return values
# syntax
"""
def fname(arg1,arg2,.....,argn):
        S.B

fname(val1,val2,......,valn)
"""
# q1.wap to get the following output

# s='python'
# out='ptoyhn'

# or method
# def extract_char(s):
#     print(s[::2]+s[1::2])

# def extract_char(s):
#     even=''
#     odd=''
#     for i in range(0,len(s)):
#         if i%2==0:
#             even+=s[i]
#         else:
#             odd+=s[i]
#     output=even+odd
#     print(output)

# extract_char('python')


# q2.wap to get the following output
# s='1234567'
# out='2461357'

# def extract_char(s):
#     even=''
#     odd=''
#     for char in s:
#         if int(char)%2==0:
#             even+=char
#         else:
#             odd+=char
#     print(even+odd)

# extract_char(s)

# 3. function wihtout args and with return values
# syntax
"""
def fname():
---------
    S.B
----------
return val1,val2,val3,......,valn

var1,var2,var3,.....,varn=fname()
print(val1,val2,....,valn)

#return multiple values in single variable as store as tuples
var=fname()
print(var)
here var is act as tuples
or 
print(fname())    
"""

# q.sample
# def sam():
#     a=int(input())
#     b=int(input())
#     return a+b,a-b,a*b,a//b

# var=sam()
# print(var)

# q1.wap to check whether the given number is armstrong or not

# def armstrong_num():
#     org=int(input('enter the num:'))
#     num=org

#     length=len(str(num))
#     sum=0
#     while num>0:
#         rem=num%10
#         sum+=rem**length
#         num//=10
#     return sum,org

# sum,num=armstrong_num()
# print(sum,num)
# if sum==num:
#     print('armstrong number')

# else:
#     print('not armstrong number')


# def armstrong_num():
#     org = int(input("enter the num:"))
#     num = org

#     length = len(str(num))
#     sum = 0
#     while num > 0:
#         rem = num % 10
#         sum += rem**length
#         num //= 10

#     if sum == org:
#         return "armstrong number"
#     else:
#         return "not armstrong number"


# print(armstrong_num())


#q3 wap to print all the prime number b/w 2 to 100
# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     else:
#         return True
            
# def prime_number():
#     #num=int(input('enter the num:'))
#     list=[]
#     for i in range(2,100):
#         if is_prime(i):
#             list.append(i)
            
#     return list

# print(prime_number())   


        
#4. function with args and with return values
'''

def fname(val1,val2,...,valn):
-----
sb
--------
return val1,val2...,valn

print(fname(val1,val2,.....,valn))

'''
#q1.wap to extract only non defult values from the given list
# l=[90,80,0.0,0j,False,'hii',7+8j,'',[],{}]
# out=[90,80,'hii',7+8j]

# def extract_ndv(l,out=[]):
#     for i in l:
#         if bool(i):
#             out.append(i)

#     return out

# l=[90,80,0.0,0j,False,'hii',7+8j,'',[],{}]
# out=[]
# print(extract_ndv(l,out))

#2. wap to check whether a num is spy number or not

# num=123
# sum=1+2+3-->6
# prod=1*2*3-->6

def check_spy(num):
    org=num
    sum=0
    prod=1
    while num>0:
        rem=num%10
        sum+=rem
        prod*=rem
        num//=10
    
    if sum==prod:
        return 'number is spy num'
    else:
        return 'number is not spy num'
    
print(check_spy(int(input('enter a num:'))))
        
        