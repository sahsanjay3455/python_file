'''
#comprehension 
# it is the process of creating mutable collection by using single line of instruction
comprehension is possible only for mutable collection (list,set,dict) because we can modify the existing data.
types of comprehension

1.list comprehension:it is the process of creating the new list collection by using the single line instruction
syntax:
1st priority-->loops
2nd priority-->conditions
3rd priority --> storing values

1.var=[val for var in collection]
2.var=[val for var in collection if condition]
3.var=[TSB if condition else FSB for var in collection ]
4.var=[var1 for var1 in collection for var2 in collection.... if condition]



2.set  comprehension:
it is the process of creating the new list collection by using the single line instruction
syntax:
1st priority-->loops
2nd priority-->conditions
3rd priority --> storing values

1.var={val for var in collection}
2.var={val for var in collection if condition}
3.var={TSB if condition else FSB for var in collection ]
4.var={var1 for var1 in collection for var2 in collection.... if condition}

3.dict comprehension:it is the process of creating new dict collection by using single line of instruction

#zip():it is used to iterate through multiple collection simultaneously
1.no of var should be eqaul to no of collecton
2.no of iteration will be eqaul to length of smallest collection
l1=[10,20,30,40,50]
l2=[100,200,300,400,500]
for i,j in zip(l1,l2):
    print(i,j) 
    
l1=[10,20,30,40,50]
l2=[100,200,300]
for i,j in zip(l1,l2):
    print(i,j) 
    
     
syntax:
i var={k:v for var in collection}---->1--collection
ii. var={k:v for var1,var2 in zip(col1,col2)}-->2 collection
iii. var={k:v for var in collectio if condition}
iv. var ={k:v1 if cond.. else v2 for var in collection  }




'''
#q1. wap to store n natural numbers from 1 to 20
# num=int(input('enter  a num:'))
# out=[i for i in range(1,num+1)]
# print(out)
#or in single line

# print([i for i in range(1,int(input('enter  a num:'))+1)])

#q2. wap to store all the even number b/w 1 to 100 in a list
# print([i for i in range(1,int(input('enter  a num:'))+1) if i%2==0])

#q3.wap to store the square of all even numbers and cube of all odd number from 1 to 100
# print([i**2 if i%2==0 else i**3 for i in range(1,int(input('enter  a num:'))+1)])

#q4.wap to get the following output
# s='program on list compr'.split()
# out=[7,'no','tsil',5]

# print([i[::-1] if len(i)%2==0 else len(i) for i in s])

#q5. wap to get the following output

# s='hai'
# out=[('h',0),('h',1),('h',2),('a',0),('a',1),('a',2),('i',0),('i',1),('i',2)]

# print([(i,j) for i in s for j in range(0,len(s))])

#2.set  comprehension:

#q1.wap to store square of all natural number 1 to 50

#q2. wap to store all the prime number b/w 1 to 100
# print({n for n in range(2, 101) if all(n % i != 0 for i in range(2, int(n**0.5) + 1))})
# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     else:
#         return True
    
# print({i for i in range(2,100) if is_prime(i)})

#q3. wap to print the sequence of armstrong number
# def is_armstrong(n):
#     num=n
#     sum=0
#     while n>0:
 
 
#  3.dict comprehension: 
# l1=[10,20,30,40,50]
# l2=[100,200,300]
# for i,j in zip(l1,l2):
#     print(i,j)      
       
#q1. wap to create a dict where n natural numbers acts as keys and square of natural number acts as values
# n=5 
# out={1:1,2:4,3:9,4:16,5:25}

# n=int(input('enter a num:'))
# print({i:i**2 for i in range(1,n+1)})
#q2. wap to get the following output
# l1=['a','b','c','d']
# l2=[100,200,300,400]
# out={'a':100,'b':200,'c':300,'d':400}

# ii. var={k:v for var1,var2 in zip(col1,col2)}-->2 collection
    
# print({k:v for k,v in zip(l1,l2) })

#q3. wap to get the following output
# iii. var={k:v for var in collectio if condition}
# s='hai helLO'
# out={'H':72,'L':76,'O':79}
# print({i:ord(i) for i in s if 'A'<=i<='Z'  })
        
#q4. wap to get the following output
# out={1:1,2:4,3:27,4:16,...}
# iv. var ={k:v1 if cond.. else v2 for var in collection  }

# print({ i:i**2 if i%2==0 else i**3 for i in range(1,int(input('enter a num:'))+1)})

#q5.  wap to get the following output

# l=[['Banglore',8000],['mumbai',6000],['Hyderabad',5000],['pune',4000],['bhubaneshwar',7000]]

#i fetch the location and rent where the rent is less than 7000
# print({i[0]:i[1] for i in l if i[1]<7000})

#ii fetch the location and rent where the rent is more than 5000
# print({i[0]:i[1] for i in l if i[1]>5000})

#iii. fetch the location and rent where the location is starting with b
# print({i[0]:i[1] for i in l if i[0][0] in ['B','b']})




