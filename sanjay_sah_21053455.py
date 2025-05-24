# '''
# q1.wap to keep summing the digits of a number until a single digit is left.
#  Example: 9875 → 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2
# '''

# num = int(input("Enter the number: "))

# while num >= 10:
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     num = sum

# print("Single digit sum is:", num)




# '''
# q2.Write a program to print the following series till n terms.
#  2, 22, 222, 2222 _ _ _ _ _ n terms
# Input1: n = 4
# Output1: 2, 22, 222, 2222
# Input2: n=3
# Output2: 2,22,222
# '''


num = int(input("enter a number: "))

for i in range(1, num + 1):
    temp = int("2" * i)  
    print(temp, end=", " if i < num else "\n")
        
    
    
    
    

# '''
# q3.3) Write a program to get the following output
#  input=[‘jiocinema.com’ , ’file.py’ , ‘web.html’ , ‘amazon.com’ , ‘text.py’]
#  output= {‘com’: [‘jiocinema’, ‘amazon’], ’py’:[ ‘file’ , ‘text’] , ‘html’:[‘web’]}
#  input_list = ['jiocinema.com', 'file.py', 'web.html', 'amazon.com', 'text.py']
# '''


# input_list = ["jiocinema.com", "file.py", "web.html", "amazon.com", "text.py"]
# output = {}

# for item in input_list:
#     sp = item.split('.')
#     key = sp[-1]
#     value = sp[0]
#     if key not in output:
#         output[key] = [value]
#     else:
#         output[key].append(value)

# print(output)


# '''
# q4.4) wap to check the given number is Armstrong or not without using type casting.
# Input: n= 153
# Output: 1**3 + 5**3+ 3**3 = 153 (Armstrong)


# '''

# def armstrong_number(num):
#     org=num
#     string=str(num)
#     length=len(string)
#     sum=0
#     while num>0:
#         rem=num%10
#         sum+=rem**length
#         num//=10

#     if org==sum:
#         return 'armstrong number'
#     else:
#         return 'not armstrong number'

# num=int(input('enter a number:'))
# print(armstrong_number(num))




# '''
# q5.5) wap to find all elements that appear more than once in a list.
# # Input: [4,3,2,7,8,2,3,1] → Output: [2,3]
# '''


# l=eval(input('enter the data in list:'))

# result=[]
# for item in l:
#     cnt=0
#     for i in range(0,len(l)):
#         if item==l[i]:
#             cnt+=1
#     if cnt>1:
#         if item not in result:
#             result.append(item)

# print('elememts present more than one time:',result)


# '''
# q6.6) wap to get the following output
# Input: [100,200,50,400,300]
# N=300
# Out = [[100,200],[300]]
# Sum of any two numbers in a list should be equal to N
# Or Any number in a list should be equal to N
# '''



# list1 = eval(input("enter the data in list:"))
# result = []
# for index in range(0, len(list1) - 1):
#     n = list1[index] + list1[index + 1]
#     if n in list1:
#             result.append([list1[index],list1[index + 1]])
#             result.append([n])

# print(result)



# '''
# q7.7) wap in functions to get the following output
# Input: ‘bacbcaabbaa’
# Output: ‘b4a5c2’
# '''


# def cout_char(str1):
#     result = ""
#     for char in str1:
#         cnt = 0
#         if char not in (result):
#             for char1 in str1:
#                 if char == char1:
#                     cnt += 1
#             result += char + str(cnt)

#     return result


# str1 = input("enter the string:")
# print(cout_char(str1))


# '''
# 8) write a function to check whether the given number is a strong number or not
# N= 145 → 1!+4!+5!= = 145
# '''


# def strong_number(num):
#     str1=str(num)
#     sum=0
#     for char in str1:
#         fact=1
#         for i in range(1,int(char)+1):
#             fact*=i
#         sum+=fact

#     if sum==num:
#         return('number is strong')
#     else:
#         return ('number is not strong')


# num=int(input('enter the num:'))
# print(strong_number(num))


# '''

# 9) wap to get the following output
# L = [‘hai’, 34, 3.4, ‘hello’, 90, ‘byebye’]
# Out = {‘hai’: ‘hi’, ‘hello’ :’ho’, ‘byebye’: ‘be’}

# L = ['hai', 34, 3.4, 'hello', 90, 'byebye']
# output={}
# for item in L:
#     if type(item)==str:
#         fl=item[0]+item[-1]
#         output[item]=fl

# print(output)


# '''
# 10) wap to find maximum value present in a list without using any sorting
# functions.
# '''
# list1=eval(input('enter the list data:'))

# max_val=0
# for item in list1:
#     if item>max_val:
#         max_val=item

# print('maximum value present in the list is:',max_val)
