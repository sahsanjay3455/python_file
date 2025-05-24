"""
lambda:
1.it is the keyword which is used to solve the simple calcualtion
2.we can solve the if , if--else problems using lambda
3.lambda is an anonumous or nameless function (calling is not possible)
4.we have to store the lambda expression into a variable
5.it helps us to write the code in a single line

syntax 1:
var=lambda agr1,arg2,....,agrn:expression
    print(val(value))

syntax 2:
var=lambda args:TSB if cond else FSB
print(var(value))
"""

# q1.wap to check a num is even or not using lambda

# even=lambda num: num%2==0
# print(even(int(input('enter the val:'))))

# q2. wap to check whether the given string is palindrome or not

# val=lambda str:str==str[::-1]
# reslt=val(('level'))
# if reslt:
#     print('palindrome no')
# else:
#     print('not palindrome no')

# q3. wap to check whether the given data is mutuable or not using lambda function

# mut = lambda data: "Mutable" if type(data) in [list, dict, set] else "Immutable"

# print(mut([1, 2, 3]))      # Mutable
# print(mut((1, 2, 3)))      # Immutable
# print(mut({'a': 1}))       # Mutable
# print(mut("hello"))        # Immutable
# print(mut({1, 2, 3}))      # Mutable

# q4. wap to convert the char into upper case
# upper=lambda char:char.upper()

# print(upper(input('enter the char:')))

# q5 wap to find the ascii value of a given char

# val=lambda char:ord(char)
# print(val(input('enter the char:')))

# syntax 2:
# var=lambda args:TSB if cond else FSB
# print(var(value))


# q6. wap to check whether the last digit of an interger is 5 or not

# ld = lambda num: "yes" if num % 10 == 5 else "No"
# print(ld(int(input("enter the num:"))))

# q7 wap to print length of the string if it is palindrome or else print reverse of string

# var=lambda str:len(str) if str==str[::-1] else str[::-1]
# print(var('level'))


# q8 wap to check whether a given string is a keyword or not
# import keyword

# s = lambda str: "keyword" if str in keyword.kwlist else "not keyword"

# print(s("int"))
# # print(s('hello'))

# q9 wap to take two string as input . return the conacatenatd output if both have same length else return concatenated output of starting chars from both strings

# concate=lambda str1,str2: str1+str2 if len(str1)==len(str2) else str1[0]+str2[0]
# str1=input('enter 1st string:')
# str2=input('enter 1st string:')

# print(concate(str1,str2))

#sorted by lambda function
# sorted fucntion
# l = [10, 90, 78, 5]
# print(sorted(l)) #--ascending order
# print(sorted(l,reverse=True)) #descending order

# l=['hello','Kiit','Good','Hai']
# l=[('yash',30),('raj',7),('ram',89)]
# print(sorted(l,key=lambda t:t[1]))

# l = [("rice", 30), ("dal", 7), ("fruits", 89), ("speices", 90)]
# print(sorted(l, key=lambda t: t[1], reverse=True))


# l=('eye','level','hello','kiit','apple','umbrella')

# print(sorted(l,key=lambda s:s[0] in ('aeiouAEIUO'),reverse=True))

'''
solution are done by sir

sorted(l,key=lambda s: s.isupper(),reverse=True)
['HAI', 'KIIT', 'hello', 'Good']



l=[('yash',21),('swaroop',18),('john',30)]
sorted(l,key=lambda t:t[1])
[('swaroop', 18), ('yash', 21), ('john', 30)]



l=[('rice',300),('dal',250),('fruits',500),('spices',56)]
sorted(l,key=lambda t:t[1])
[('spices', 56), ('dal', 250), ('rice', 300), ('fruits', 500)]
sorted(l,key=lambda t:t[1],reverse=True)
[('fruits', 500), ('rice', 300), ('dal', 250), ('spices', 56)]

l=('eye','level','hello','kiit','apple','umbrella')
sorted(l,key=lambda s: s[0] in 'aeiouAEIOU')
['level', 'hello', 'kiit', 'eye', 'apple', 'umbrella']
sorted(l,key=lambda s: s[0] in 'aeiouAEIOU',reverse=True)
['eye', 'apple', 'umbrella', 'level', 'hello', 'kiit']

'''