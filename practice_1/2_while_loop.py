# q1. wap to print 'kiit is a good college' for 100 times
# for i in range(0,100):
#     print('kiit is a good college')
# i = 0
# while i < 100:
#     print("kiit is a good college")
#     i+=1

# q2. wap to print even number
# num = int(input("enter number to print even:"))
# i = 1
# while i <= num:
#    print(i,end=' ')
#    i+=2


# q3.wap to print multiplication table using while loop dynamically

# num = int(input("enter a table num:"))
# i = 1
# while i <= 10:
#     print(f"{num}*{i}={num*i}")
#     i += 1

# q4. wap to find the sum of natural number:

# num=int(input('enter the num:'))
# sum=0
# i=1
# while i<=num:
#     sum+=i
#     i+=1

# print('sum of natural num is:',sum)

# q5. wap to find the factorial for given num
# num=int(input('enter the num:'))
# fact=1
# i=1
# while i<=num:
#     fact*=i
#     i+=1

# print(f'factorial of {num}! is:{fact}')

# for i in range(1,num+1):
#     fact*=i

# print(f'factorial of {num}! is:{fact}')

# q6. wap to get the following output
# s='we are kiit students we are the best developer'
# output='we_are_kiit_students_we_are_the_best_developer'
# out=''
# i=0
# while i<len(s):
#     if s[i]==' ':
#         out+='_'
#     else:
#         out+=s[i]
#     i+=1


# print(out)

# q7.wap to extract lower case from the given string
# s = "Hello How ARE You?"
# out = ""
# i = 0
# while i < len(s):
#     if "a" <= s[i] <= "z":
#         out += s[i]
#     i += 1

# print(out)

# q8. wap to extact the special case character from the given string
# s='Kiit %%^& is 78!@#$ us $%^hhhh'
# out=''
# i=0
# while i<len(s):
#     if not('a'<=s[i]<='z' or 'A'<=s[i]<='Z' or '0'<=s[i]<='9'):
#         out+=s[i]
#     i+=1
# print(out)

# q9. wap to extract only integer from a given list
# l = [10, 44, 5.6, True, 567, "kiit", [1, 2, 3, 4, 5]]
# out = [10, 44, 567]
# list = []
# i = 0
# while i < len(l):
#     if type(l[i]) == int:
#         list.append(l[i])
#     i += 1

# print(list)

# q10. wap to get the following output

# l=[10,20,True,'hello','eye','level','malayalam']
# out=['eye','level','malayalam']
# output=[]
# i=0
# while i<len(l):
#     if type(l[i])==str:
#         if l[i]==l[i][::-1]:
#             output.append(l[i])
#     i+=1

# print(output)

# q11. wap to sum of individual values of an integer without using type casting
# num = 123
# out=(1+2+3)-->6
# sum = 0
# string = str(num)
# i = 0
# while i < len(string):
#     sum += int(string[i])
#     i += 1
# print("sum of individual digit is:", sum)

# alternate method
# while num > 0:
#     sum += num % 10
#     num //= 10

# print("sum of individual is:", sum)

# q12. wap to remove duplicate values form a given list without using set
# list1 = [10, 20, 30, 10, 20, 30, 10]
# out = []

# i = 0
# while i < len(list1):
#     if list1[i] not in (out):
#         out.append(list1[i])
#     i += 1

# print(out)
# for item in list1:
#     if item not in (out):
#         out.append(item)

# print(out)
# q13.wap to left rotation by k
# list1 = [10, 20, 30, 40, 50]
# k = 2
# new_list=list1[k::]+list1[:k:]
# print(new_list)
