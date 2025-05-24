# q1.wap to check username and password are correct or not
# og_username='sanjaysah'
# og_password='sanjay@123'
# while True:
#     username=input('enter username:')
#     if username==og_username:
#         pwd=input('enter password:')
#         if pwd==og_password:
#             print('login successfully✅')
#             break
#         else:
#             print('password is incorrect ❌')
#     else:
#         print('username is incorrect❌')


# q2.wap to check interger is   1digit,2digit ,3digit and more than 3digti

# num = int(input("enter the number:"))
# new_string = str(num)
# if num>0:
#     string = new_string    
# else:
#     string=new_string[1::]
    
    
# print(string)
# length = len(string)

# if length == 1:
#     print(f"{num} is {length} length")

# elif length == 2:
#     print(f"{num} is {length} length")

# elif length == 3:
#     print(f"{num} is {length} length")

# elif length > 3:
#     print(f"{num} is {length} length")

#alternate method
# num = int(input("enter the number:"))

# if 0<=num<=9 or  -9<=num<=0:
#     print('1 digit num')
# elif 10<=num<=99 or -99<=num<=-10:
#     print('2 digit num')
# elif 100<=num<=999 or -999<=num<=-100:
#     print('3 digit num')
# else:
#     print('num is more than 3 digit')

#q3. wap to find the greatest num among three number

# a=int(input('enter the first num:'))
# b=int(input('enter the second num:'))
# c=int(input('enter the third num:'))

# if a>=b and a>=c:
#     print(f'{a} is greater number:')
# elif b>=a and b>=c:
#     print(f'{b} is greater number:')
# else:
#     print(f'{c} is greater number:')
