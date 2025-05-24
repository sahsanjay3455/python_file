# str='sanjay'
# for char in str:
#     print(ord(char))

# org=int(input('enter a num:'))
# num=org

# result=0
# while num>0:
#     rem=num%10
#     num//=10
#     fact=1
#     for i in range(1,rem+1):
#         fact*=i
#     result+=fact
    
# print(result)  
# if result==org:
#     print('num is strong')
# else:
#     print('not strong number')

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact

# num=int(input('enter the number:'))
# print(factorial(num))

def replacement(s,out=''):
    for char in s:
        if char=='1':
            out+='0'
        elif char=='0':
            out+='1'
        else:
            out+=char
    return out

print(replacement('11100000#$%^&'))

