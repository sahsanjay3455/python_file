# pass
# a=10
# if a==10:
# error will throw so prevent error we will "pass" keyword
# a=10
# if a==10:
#     pass

# break
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)

# q1. wap to check whether the given num is prime or not
n=int(input('enter a num:'))
for i in range(2,n):
    if n%i==0:
        print('not a prime:')
        break
else:
    print('prime number')
    

# q2. develop a dynamic login functionality
og_username = 'sanjaysah'
og_password = 'sanjay@123'

while True:
    uname = input('Enter your username: ')
    if og_username == uname:
        pwd = input('Enter your password: ')
        if pwd == og_password:
            print('✅ Login successful!')
            break
        else:
            print('❌ Incorrect password. Try again.')
    else:
        print('❌ Incorrect username. Try again.')


# q3. wap to develop guessing a number game

import random
#random.randint(sv,ev)

print('guess a number b/w 1 to 100')
num=random.randint(1,100)
while True:
    guess=int(input('enter a num:'))
    if guess > num:
        print('your num is greater')
    elif guess < num:
        print('your num is lesser')

    else:
        print('you are right')
        print('you won the game')
        break

# q4. wap to check whether a string is haing all lowercase or not

s = 'Hello'
s = 'sanjay'

for i in s:
    if not ('a' <= i <= 'z'):
        print('Not all characters are in lowercase')
        break
else:
    print('All characters are in lowercase')

# q5 . wap to check whether the collection are homo or hetero

l=[10,20,30,3.5,6.7,True]
l=[10,20,30,40]
dt=type(l[0])
for val in l:
    if dt!=type(val):
        print('hetero data')
        break
else:
    print('homo data set')


# continue
# demo
for i in range(1,11):
    if i==3 or i==7:
        continue
    print(i)
# q1. wap to print all the odd number between 1 to 100 using continue

for i in range(1,100):
    if i%2==0:
        continue
    print(i)

# q2. wap to extract all the upper case char from a given string

s='SanJaY saH from NepaL'
out=''
for i in s:
    if not ('A'<=i<='Z'):
        continue
    out+=i

print(out)

# q3. wap to get the following output

s1 = "1110010100"
s2 = "1100010001"
out = 2

cnt = 0

if len(s1) == len(s2):
    for i in range(0, len(s1)):
        if s1[i] == s2[i]:
            continue
        cnt += 1

else:
    print("length is difference")

print(cnt)







