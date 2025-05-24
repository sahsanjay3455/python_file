#1.wap to check username and password are correct

og_username='yash123'
og_password='yash@123'

uname=input('enter the username:')
if uname==og_username:
    pwd=input('enter the password:')
    if pwd==og_password:
        print('login successfully✅')
    else:
        print('Incorrect password ❌')    
else:
    print('Incorrect username ❌')        
    
#q2. wap to print the middle character of the string only if it it is uppercase
#'good'

str_input = input('Enter the string: ')

if len(str_input) % 2 != 0:
    mid = str_input[len(str_input) // 2]
    if 'A' <= mid <= 'Z':
        print(f'Middle character is {mid}')
    else:
        print('Middle character is not uppercase')
else:
    print('Length is an even number')
