# nested for loop
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,j)

# q1.wap to get the following output

s = "mission impossible".split()
out = {"mission": 7, "impossible": 10}
output = {}
for word in s:
    length = 0
    for char in word:
        length += 1
    output[word] = length

print(output)

# q2. wap to get the following output
s='power star'.split()
out={'power':2,'star':1}
output={}

for word in s:
    length=0
    for char in word:
        if char in('aeiouAEIOU'):
            length+=1
    output[word]=length

print(output)

# q3. wap to check whether a given integer is strong or not

num=int(input('enter the number:'))
s=str(num)
sum=0
for char in s:
    sum1=1
    for i in range(1,int(char)+1):

        sum1=sum1*i
    sum+=sum1

if sum==num:
    print('strong num')
else:
    print('not a strong num')


# q4. wap to get the following output

s = "bacbcaabbccc"
out = "b4a3c5"

output = ""

for i in s:
    cnt = 0
    for j in s:
        if i == j:
            cnt += 1

    if i not in output:
        output += i + str(cnt)

print(output)


# q5. wap to get the following output

s = {10: "star", 20: "bye", 30: "moon", 40: "apple"}
out = {10: "a", 20: "e", 30: "oo", 40: "ae"}

output = {}
for i in s:
    val=s[i]
    char=''
    for j in val:
        if j in 'aeiouAEIOU':
            char+=j
    output[i]=char        
        
print(output)       
