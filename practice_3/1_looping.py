# #1.wap to check the chararact is vowel or not
# char1=input('enter the char:')
# if char1 in ('aeiouAEIOU'):
#     print('char is vowel')
# else:
#     print('char is not vowel')

# #2.wap to check the chararact is consonent or not
# char1=input('enter the char:')
# if char1 not in ('aeiouAEIOU'):
#     print('char is consonent')
# else:
#     print('char is not consonent')

# #3.wap to check the given data is float type or not
# data=eval(input('enter a data:'))

# if type(data)==float:
#     print('data is float')

# else:
#     print('data is not float')

# 4.wap to check the given collection is mutable or not

# hints: list,set and dict are mutable data type

# var=eval(input('enter the collection:'))
# print(type(var))

# if type(var) in([list,set,dict]):
#     print('collection is mutable')
# else:
#     print('collection is not mutable')


# 5.wap to check the given number is even or not
# num=int(input('enter the num:'))

# if num%2==0:
#     print('num is even:')
# else:
#     print('num is not even')

# 6.wap to extract upper case,lower case,digit and special chars

# string='sanJAY3455@#*&^'
# upper_case=''
# lower_case=''
# digit=''
# special_char=''

# for char in string:
#     if 'A'<=char<='Z':
#         upper_case+=char
#     elif 'a'<=char<='z':
#         lower_case+=char
#     elif '0'<=char<='9':
#         digit+=char
#     else:
#         special_char+=char

# print('upper case:',upper_case)
# print('lower case:',lower_case)
# print('digit:',digit)
# print('special char:',special_char)

# 7.wap to check the given string is palidrome or not
# by using slicing
# string = input("enter the string:")

# if string == string[::-1]:
#     print("given string is palindrome")
# else:
#     print("given is not palindrome")

# by using without slicing
# def is_palindrome(string):
#     rev = ""
#     for char in string:
#         rev = char + rev

#     if rev == string:
#         print("given string palindrome")
#     else:
#         print("given string is not palindrome")


# num=int(input('enter the no of test case:'))
# for i in range(1,num+1):
#     string=input('enter the string:')

# 8.wap to find that number is 1digit , 2digit , 3digit or more than that
# num=int(input('enter the num:'))

# string=''
# if num>=0:
#     string+=str(num)
# else:
#     string+=str(num)[1::]

# print(len(string))
# if len(string)==1:
#     print('1digit num:')
# elif len(string)==2:
#     print('2digit num:')
# elif len(string)==3:
#     print('3digit num')
# else:
#     print('more than 3 len')

# 9.wap to find the sum of natural num
# n(n+1)/2
# num=int(input('enter the num:'))
# sum=0

# for i in range(1,num+1):
#     sum+=i

# print('sum of natural number is:',sum)

# 10.wap to find the factorial number
# num=int(input('enter the number:'))

# fact=1
# for i in range(1,num+1):
#     fact*=i

# print('factorial number is:',fact)

# 11.wap to sum of indivisual digit

# num=123-->1+2+3-->6
# num=int(input('enter the number:'))
# sum=0

# while num>0:
#     sum+=num%10
#     num//=10

# print('sum of individaul is:',sum)

# 12.wap to check the armstrong number
# num=153-->1^3+5^3+3^3-->1+125+27-->153
# num=int(input('enter the num:'))

# l=len(str(num))
# print('length is:',l)
# sum=0
# org=num
# while num>0:
#     sum+=(num%10)**l
#     num//=10

# if org==sum:
#     print('given number is armstrong num:')
# else:
#     print('given number is not armstrong num:')

# 13.wap to remove the duplicate values from the list without using set
# col=eval(input('enter the list:'))
# #input : [1,2,3,2,3,3,5,6]
# #out:[1,2,3,5,6]

# out=[]
# for var in col:
#     if var not in(out):
#         out.append(var)

# print('distint element is:',out)

# 13.wap to exact all even number from the tuple
# col=eval(input('enter the element in the tuple:'))
# t=()
# for var in col:
#     if var%2==0:
#         t+=(var,)

# print(t)


# 14.wap as given
# input: s='icon star'
# out: {'icon':4,'star':4}

# string = input("enter the string:").split()
# dict1 = {}

# for word in string:
#     dict1[word] = len(word)

# print(dict1)


# 15.wap as given ouput
# Input: ['jiocinema.com','flipkart.in','file.py','index.html','file.java','file.com','file2.java','amazon.com']
# l = [
#     "jiocinema.com",
#     "flipkart.in",
#     "file.py",
#     "index.html",
#     "file.java",
#     "file.com",
#     "file2.java",
#     "amazon.com",
# ]
# output: {'com':['jiocinema','file','amazon'],'in':['flipkart'],'py':['file'],'html':['index'],'java':['file','file2]}

# output = {}
# for var in l:
#     sp = var.split(".")
#     key = sp[1]
#     value = sp[0]
#     if key not in output:
#         output[key] = [value]

#     else:
#         output[key].append(value)

# print(output)
