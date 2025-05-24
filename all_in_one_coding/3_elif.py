#1.wap to check wether the char is upper , lower,digit or special char

char=input('enter the char:')
if 'A'<=char<='Z':
    print('upper case:')
    
elif 'a'<=char<='z':
    print('lower case')    
    
elif '0'<=char<='9':
    print('digit case')   
    
else:
    print('special case')    


#2 wap to check a given integer is 1digit , 2digit , 3 digit or more than 3 digit 

#also can be done by type casting

# num=int(input('enter a number:'))
# if num>=-9 and num<=9:
#     print('1 digit number')
    
# elif 10<=num<=99 or -99<=num<=-10:
#     print('2 digit number')    

# elif 100<=num<=999 or -999<=num<=-100:
#     print('3 digti number')    
 
# else:
#     print('more than 3 digits')    

#3.wap to check greater among 3 number

a=int(input('enter first num:'))
b=int(input('enter second num:'))
c=int(input('enter third num:'))


if a>=b and a>=c:
    print(f'{a} is greater num')
elif b>=a and b>=c:
    print(f'{b} is greater number')    
    
else:
    print(f'{c} is greater number')  
     