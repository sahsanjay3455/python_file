"""
take one dict from user key- your friend name , values-marks/score
1.find the maximum score pair without using max()
2.find the minimum score pair without using min()
3. sort dict based onn values(score) without using sort()--- ascending
4. take name from user check the name is already present
or not if not ask value from user add this pair(key,value) to dict
5.remove least scor pair

"""

# q1.find the maximum score pair without using max()
# num = int(input("enter the no of student:"))
# dict = {}

# for i in range(0, num):
#     name = input("enter the studnet name:")
#     mark = int(input("enter the student mark:"))
#     dict[name] = mark


# max_mark = 0
# max_key = ""
# for k, v in dict.items():
#     if v > max_mark:
#         max_mark = v
#         max_key = k

# print(f"maximum score pair is :{max_key}:{max_mark}")


# q2.find the minimum score pair without using min()

# num = int(input("enter the no of student:"))
# dict = {}

# for i in range(0, num):
#     name = input("enter the studnet name:")
#     mark = int(input("enter the student mark:"))
#     dict[name] = mark


# min_mark = float('inf')
# min_key = ""
# for k, v in dict.items():
#     if v < min_mark:
#         min_mark = v
#         min_key = k

# print(f"minimum score pair is :{min_key}:{min_mark}")


#q3. sort dict based onn values(score) without using sort()--- ascending

num = int(input("enter the no of student:"))
dict = {}

for i in range(0, num):
    name = input("enter the studnet name:")
    mark = int(input("enter the student mark:"))
    dict[name] = mark
    
# min_value=dict.values()[0]
# min_key=dict.keys()[0]


# for i in dict:
#     if dict[i]<min_value:
#         min_value=dict[i]
#         min_key=dict[]
result={}        
while dict:
    min_key=list(dict.keys())[0]
    min_val=list(dict.values())[0]
    for i in dict:
        if dict[i]<min_val:
            min_val=dict[i]
            min_key=i
            
    result[min_key]=min_val
    del dict[min_key]
    
print(dict,result)  
print('max element is:',result.popitem())         
print(list(result.items())[0])            