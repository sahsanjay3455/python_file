#Recursion:it is  process of calling the function by itself until the given termination become true
# def sam(n=5):
#     if n<=0:#termination condition
#         return
    
#     print('hello')
#     sam(n-1) #recursion call
    
# sam()#main function call

#syntax:
'''
def fname(args):
    if terminatin cond:
    return val
---------------
sb
---------
    return fname(args)
    
print(fname(values))


'''

#q1.finding the factorail number

# def fact(n):
#     if n==0 or  n==1:
#         return 1
    
#     return n*fact((n-1))


# num=int(input('enter a number:'))
# print(fact(num))



# converting looping program into recursion
'''
1.initialization of looping variable should be done in formal argument section
2.Termination condition should be exactly opposite to looping condition
>------<=
<------->=
3.return final result inside if statement
4.mention logic as it is by ignoring looping condition and updation
5.updation should be done in recursive call

'''

#q1. wap to extract lowercase char from a given string
# s='Hello'
# out=''
# i=0
# while i<len(s):
#     if 'a'<=s[i]<='z':
#         out+=s[i]
#     i+=1
    
# print(out)

#by using recursin

# def ex_low(s,out='',i=0):
#     if i>=len(s):
#         return out
#     if 'a'<=s[i]<='z':
#         out+=s[i]
    
#     return ex_low(s,out,i+1)

# print(ex_low(s))

#q2.wap to get the following output
# s='1001010101#@!'
# out='0110101010#@!'
# output=''
# i=0
# while i<len(s):
#         if s[i]=='1':
#             output+='0'
#         elif s[i]=='0':
#             output+='1'
#         else:
#             output+=s[i]
        
# print(output)

#by using recursion

# def extract_char(s,output='',i=0):
#     if i>=len(s):
#         return out
#     if s[i]=='1':
#         output+='0'
#     elif s[i]=='0':
#         output+='1'
#     else:
#         output+=s[i]
        
#     return extract_char(s,output,i+1)

# print(extract_char(s))