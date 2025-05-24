# q1.wap to get the following output
# s = "mission impossible".split()
# out = {"mission": 7, "impossible": 10}
# output = {}
# for word in s:
#     cnt = 0
#     for char in word:
#         cnt += 1
#     output[word] = cnt


# print(output)

# q2.wap to get the following output
# s = "power star".split()
# out = {"power": 2, "star": 1}
# result = {}
# for word in s:
#     cnt = 0
#     for char in word:
#         if char in ("aeiouAEIOU"):
#             cnt += 1
#     result[word] = cnt

# print(result)

# q3.wap to check whether a given integer is strong or not
# num=145--->1!+4!+5!-->1+24+120=>145
# num=int(input('enter the number:'))
# str=str(num)
# sum=0
# list=[]
# for char in str:
#     fact=1
#     for i in range(1,int(char)+1):
#         fact*=i
#     sum+=fact

# if sum==num:
#     print('strong number:')
# else:
#     print('not strong number:')

# num = int(input("enter the number:"))
# # str = str(num)

# list = []
# for digit in range(1,num):
#     str1=str(digit)
#     sum = 0
#     for char in str1:
#         fact = 1
#         for i in range(1, int(char)+1):
#             fact *= i
#         sum += fact

#     if sum == digit:
#         list.append(digit)
#         print(digit)


# print(list)

# q4 wap to get the following output
# s = "bacbcaabbccc"
# out = "b4a3c5"
# output = ""
# i=0
# for char in s:
#       if char not in output:
#         cnt = 0
#         for char1 in s:
#             if char1 == char:
#                 cnt += 1
#             i+=1
#             print(i,end=' ')
#         output += char + str(cnt)

# print(output)


# q5 wap to get the following output
# s = {10: "star", 20: "bye", 30: "moon", 40: "apple"}
# out = {10: "a", 20: "e", 30: "oo", 40: "ae"}

# output = {}
# for key in s:
#     word = s[key]
#     val = ""
#     for char in word:
#         if char in ("aeiouAEIOU"):
#             val += char
#     output[key] = val

# print(output)
