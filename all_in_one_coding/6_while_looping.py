# q1. wap to print 'kiit is a good college' for 100 times

i = 0
while i < 100:
    print("kiit is a good college")
    i += 1

# q2. wap to print even number
i = 2
while i <= 100:
    print(i, end=" ")
    i += 2

# q3. wap to print multipliction table by using user table

num=int(input('enter table num:'))
i=1
while i<=10:
    print(f'{num} x {i}={num*i}')
    i+=1


# q4. wap to find the sum of n natural number
num=int(input('enter a num'))
i=1
sum=0
while i<=num:
    sum+=i
    i+=1

print('sum of natural num: ',sum)

# q5.wap to find the factorial for given num

num=int(input('enter a number:'))
fact=1
i=1
while i<=num:
    fact=fact*i
    i+=1
print(f'factorail of {num} is {fact}')

# q6. wap to get the following output

s='we are KIIT students we are the best developers'
output ='we_are_KIIT_students_we_are_the_best_developers'

i=0
s = 'we are KIIT students we are the best developers'
output = ''
i = 0
print(len(s))

while i < len(s):
    if s[i] == ' ':
        output += '_'
    else:
        output += s[i]
    i += 1

print(output)


# q7. wap to extract lower case character from the given str

s='Hello How ARE yoU?'
out='elloowyo'
output=''
i=0
while i<len(s):
    if 'a'<=s[i]<='z':
        output+=s[i]

    i+=1

print(output)


# q8. wap to extract special case character from the given str

s='Kithne #$%^&aadmi 12345678 they $%^&() sardar 6 aadmee %^&*() they'
out='elloowyo'
output=''
i=0
while i<len(s):
    if not( 'a'<=s[i]<='z' or 'A'<=s[i]<='z' or '0'<=s[i]<='9'):
        output+=s[i]

    i+=1

print(output)

# q9. wap to extract only interger from a given list

l = [10, 345, 5.6, True, 567, "KIIT", [1, 2, 3, 4, 5]]
out=[10,234,567]
output = []
i = 0
while i < len(l):
    if type(l[i]) == int:
        output.append(l[i])

    i += 1

print(output)


# q10. wap to get the following output

# l = [10, 20, True, "hello", "eye", "level", "gabber singh", "palindrom", "malayalam"]
# out=['eye','level','malayalam']
out = []

i = 0
while i < len(l):
    if type(l[i]) == str:
        if l[i] == l[i][::-1]:
            out.append(l[i])

    i += 1

print(out)


# q11. wap to sum of individual values of an integer without type casting
num = 123
# out=1+2+3-->6
s=str(num)
sum=0
i=0

while i<len(s):
    sum+=int(s[i])
    i+=1

print(sum)

# alternate method--last digit method
sum = 0
while num > 0:
    sum += num % 10
    num //= 10

print("sum is ", sum)



#q12. wap to remove duplicate values from a given list without using set

list=[10,20,30,10,20,30,10,20]
# output=[10,20,30]

i=0
out=[]
while i<len(list):
    if list[i] not in (out):
        out.append(list[i])
    i+=1 
        
print(out)        