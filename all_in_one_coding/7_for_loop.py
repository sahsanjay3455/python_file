# q1
# col = {10, 23, 4.5, True, [1, 2, 3, 4, 5], "hello"}
# col={1:'a',2:'b',3:'c',4:'d',5:'e'}
# col='good afternoo guys'
# for char in col:
#     print(char, end=" ")

# in range not need for type casting
# for i in range(1,11):
#     print(i)

# l=[1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(l)):
#     print(l[i])

# q1. wap to print all the integers present in a list
# l=eval(input('enter a list'))
# for item in l:
#     if type(item)==int:
#         print(item)


# q2 wap to find length of the collection without using len()

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# l=eval(input('enter the collection:'))
# cnt = 0
# for i in l:
#     cnt += 1

# print("length is :", cnt)


# q3 revers the string without using slicing

# s = "sanjay"
# reversed_s = ''

# for i in range(len(s) - 1, -1, -1):
#     reversed_s += s[i]

# print(reversed_s)


# alternate method
# rev = ""
# for i in s:
#     rev = i+rev

# print(rev)

# q4. wap to extract all the even numbers present in the tuples
# t = (12, 23, 24, 10, 6, 8, 35)
# out = ()
# for i in t:
#     if i % 2 == 0:
#         out = out + (i,)
# print(out)


# q5.wap to get the following output
# s='icon star'
# s=input('enter a str:').split()
# out={'icon':4,'star':4}
# dict={}

# list=s.split()
# for i in list:
#     dict[i]=len(i)
# print(dict)

# q6 wap to get the following output

# s='always keep smiling'
# out={'always':'syawla','keep':'peek','smiling':'gnilims'}

# list=s.split()
# output={}

# for i in list:
#     output[i]=i[::-1]

# print(output)

# 7 wap to get the following ouput

# l=['jiocinema.com','flipkart.in','file.py','index.html','file.java','file.com','file2.java']

# out=['com','in','py','html','java']
# output=[]

# for i in l:
#     temp=i.split('.')[-1]
#     if temp not in output:
#         output.append(temp)


# print(output)

# q8 wap to get following output

# l=['jiocinema.com','flipkart.in','file.py','index.html','file.java','file.com','file2.java','amazom.com']
# out={'com':['jiocinema','amazom'],'in':['flipkart'],'py':['file'],'html':['index'],'java':['file','file2']}

# output={}

# for name in l:
#     s=name.split('.')
#     key=s[1]
#     val=s[0]
#     if key in output:
#         output[key].append(val)
#     else:
#         output[key]=[val]

# print(output)


# q9 wap to get following output
# l = ["hai", 34, 3.4, "hello", 90, "byebye"]
# out = {"hai": "hi", "hello": "ho", "byebye": "be"}
# output = {}
# for i in l:
#     if type(i) == str:
#         output[i] = i[0]+i[-1]
# print(output)


# q10 wap to get following output
# s='HELLO'
# out={0:'H',1:'E',2:'L',3:'L',4:'O'}
# ind=0
# output={}
# for i in s:
#     output[ind]=i;
#     ind=ind+1
# print(output)
# enumerate return index and character
# for index,char in enumerate(s):
#     output[index]=char

# print(output)

# q11. wap to get following output
s = 'always keep smiling'.split()
out = "syawla peek gnilims"

output = []

# for word in s: 
#     output +=(word[::-1])+' '
# print(output.strip())

for word in s: 
    output .append(word[::-1])
    
print(' '.join(output))
