# q1.wap to print all the integers present in a list
# list = [10, "hii", 39, True, 5 + 4j, [1, 2, 3, 4], 9, 90]
# result = []
# for item in list:
#     if type(item) == int:
#         result+=[item]

# print(result)

# q2. wap to find the length of collection without using length function

# l = "sanjayuu"
# cnt = 0
# for i in l:
#     cnt += 1

# print(cnt)

# q3. wap to reverse the string without using slicing

# s = "sanjay"
# output = "yajnas"
# out = ""

# for i in s:
#     out = i + out

# print(out)


# q4. wap to extract all the even numbers present in the tuples
# t = (12, 23, 10, 6, 8, 35)
# out = ()
# for i in t:
#     if i % 2 == 0:
#         out += (i,)


# print(out)

# q5. wap to get the following output

# s = "icon star sanjay"
# output = {"icon": 4, "star": 4}
# out = {}
# sp = s.split()
# for char in sp:
#     out[char] = len(char)


# print(out)


# q6.wap to get the following output

# s = "always keep smiling".split()
# out = {"always": "syawla", "keep": "peek", "smiling": "gnilims"}
# output = {}
# for char in s:
#     output[char] = char[::-1]

# print(output)

# q7.wap to get the following output
# l = [
#     "jiocinema.com",
#     "flipkart.in",
#     "file.py",
#     "index.html",
#     "file.java",
#     "file.com",
#     "file2.java",
# ]
# output = ["com", "java", "in", "py", "html"]
# out = []
# for char in l:
#     # print(char)
#     extension = char.split(".")[-1]
#     out += [extension]

# print(out)

# q8. wap to get the following output
# l = [
#     "jiocinema.com",
#     "flipkart.in",
#     "file.py",
#     "index.html",
#     "file.java",
#     "file.com",
#     "file2.java",
# ]
# output =['com':['jiocinema','file'],'java':['file'], 'in':['flipkart'],'py':['file'],'html:['index']]

# out = {}
# for char in l:
#     key = char.split(".")[1]
#     val = char.split(".")[0]
#     if key in (out):
#         out[key] += [val]
#     else:
#         out[key] = [val]

# print(out)


# q9.wap to get the following output
# l=['hai',34,3.4,'hello',90,'byebye']
# out={'hai':'hi','hello':'ho','byebye':'be'}
# output={}
# for i in l:
#     if type(i)==str:
#         output[i]=i[0]+i[-1]

# print(output)

# q10.wap to get the following output

# s='HELLO'
# out={0:'H',1:'E',2:'L',3:'L',4:'O'}
# output={}
# for i in range(0,len(s)):
#     output[i]=s[i]

# print(output)

# q11.wap to get the following output
# s = "always keep smiling".split()
# output = "syawla peek gnilims"
# out = []
# for char in s:
#     out.append(char[::-1])

# print(" ".join(out))


