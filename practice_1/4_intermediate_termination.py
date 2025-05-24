# q1.wap to check whether the given num is prime or not

# num=int(input('enter the num:'))

# for i in range(2,num):
#     if num%i==0:
#         print('number is not prime:')
#         break

# else:
#     print('number is prime ')

# q2.wap to develop a dynamically login functionality
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

# q3.wap to develop guessing game

# import random
# num=random.randint(1,100)

# while True:
#     nw_num=int(input('enter between 1 to 100:'))
#     if nw_num>num:
#         print('you need to enter lesser number:')
#     elif nw_num<num:
#         print('you need to enter greater number:')
#     elif nw_num==num:
#         print('you are right')
#         print('you won the game')
#         break


# q4.wap to check whether a string is having all lower case or not
# s = "hellowO"
# s = "Heelo"
# for i in s:
#     if not ("a" <= i <= "z"):
#         print("all chars are not in lower case:")
#         break
# else:
#     print("all are in lower case")

# q5.wap to check whether the collections are homo or hetero
# l = [10, 20, True, 5.6, "sanjay"]
# l = [10, 20, 30, 40, 50]
# for i in l:
#     if type(l[0]) != type(i):
#         print("this is heterogeneous collection")
#         break
# else:
#     print("this is homogeneous collection")


# q6.wap to print all odd number between 1 to 100 using continue

# for i in range(1, 100):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i,end=' ')

# q7 wap to extract all the upper case char from a given string
# s='Sanjay saH from NepaL'
# str=''
# for i in s:
#     if 'A'<=i<='Z':
#         str+=i

# print(str)


# q8.wap to get the following output
# s1 = "1110010100"
# s2 = "1100010001"
# out = 3
# cnt = 0
# if len(s1) == len(s2):
#     for i in range(0, len(s1)):
#         if s1[i] != s2[i]:
#             cnt += 1
# else:
#     print("size of both string are not same")

# print(cnt)
