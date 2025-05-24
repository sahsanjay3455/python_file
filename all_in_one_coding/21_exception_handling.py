'''
#Exception_Handling:
exception:it is an unauthorized event (error) which will interrupt the program execution
#exception handling: it the process of handling the expections or error

* except syntax error remaining all are exceptions

ValuesError:if we dont pass valid variable
NameError:if any var not declare then nameError
ZeroDivisionError:
TypeError:if same dt not same

Types of expection handling:

1.specific expection handling:
if we know what errors we will get then we can use specific EH.

syntax:
try:
    -----
    problem statement
    ---------
except errorname1:
    solution

except errorname2:
    solution
    
.....
expect errornamen:
    solution
    

try block: it consist of problem statement
expect: it will handle the exception and the solution for problem must be mention here.

eg1:
try:
    a=int(input('enter a number:'))
    b=int(input('enter a number:'))
    print(a/b)
    
except ValueError:
    print('value error:should enter only interger type')
    
except ZeroDivisionError:
    print('Diving by  zero:cant divide a value by zero')
    
print('my code is here')

eg2:
try:
    a=eval(input('enter a value val1:'))
    b=eval(input('enter a value val2:'))
    print(a+b)
except NameError:
    print('name error: variable is not define')
    
except TypeError:
    print('type Error:same type of data should be enter')
print('my code is here')



2.generic expection handling:
if we know do't know what type of error that we wiil get then we can use generic Exception Handling


syntax:
try: 
    -----
    ps
    ----
    
except Exception:
     common 
     solution
     
     
note: expection class handles all type of errors  except KeyboardInterruptError
eg:
eg1.
try:
    a=int(input('enter a num:'))
    b=int(input('enter a num:'))
    print(a/b)
    
except Exception as error:
    # print('all expection got handle')
    print(f'Error name is {error} got handled')
    
print('my code is here')
print('code is done')

eg2:
try:
    while True:
        print('banana')
    
except Exception as e:
    print(f'error name is {e} got handled')
    
or

try:
    while True:
        print('banana')
        

except KeyboardInterrupt:
    print('interrupt error is handle')
    
except Exception as e:
    print(f'error name is {e} got handled')

    
print('code is here')



3.defult exception handling:
if we know do't know what type of error that we wiil get then we can use generic Exception Handling
1. default Eh will handle all the error including keyboardInterruptError

syntax:
tyr:
------
ps
----
except:
----
common
solution
------

eg:
try:
    a=eval(input('enter a val1:'))
    b=eval(input('enter a val2:'))
    print(a/b)
    
    while True:
        print('banana')
        

    
except :
    print('all errors got handled')

    
print('code is here')



different types of block:

try:
    ---
    ps
    ----
except:
    -----
    solution
    ---
else:
    alternate block (if try is not having any error then else block will execute)

finally:
  s.b   (it is indepenedent on other block )
  
  
  eg:
  
try:
    a=int(input('enter a val1:'))
    b=int(input('enter  a val2:'))
    print('sum is :',a+b)
except:
    print('all error got handled...')
    
else:
    print('program dont have any error')

finally:
    print('completed')
    print('my imp code')
    print('code is done')
    
    
    
------------------------------------------------------------------

Custom exception handling:
it the process of creating user defined errors

1.Raise:
i.creating custom exception using raise keyword:
syntax:
raise ErrorName(message)

eg1:by using class classname(Excpetion)
class outoflimit(Exception):
    pass

#game rule(2<=num<=8)
num=int(input('enter a num:'))
if num<2 or num>8:
    raise outoflimit('plz enter the num in given range')
else:
    print('entered correct:',num)
    

eg2.without class 
#game rule(2<=num<=8)
num=int(input('enter a num:'))
if num<2 or num>8:
    raise ValueError('plz enter the num in given range')
else:
    print('entered correct:',num)
    
    
2.Assert:
assert condition,message

  eg1:
s=input('enter a str:')
assert 'A'<=s[0]<='Z','first char should be uppercase'

print('string is:',s)

eg2: no should be positive

num=int(input('enter a num:'))
assert num>0,'number should be positive:'
print('correct:',num)    

'''






