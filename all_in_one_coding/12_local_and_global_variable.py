# local and global variable and its scopes
# global variable : outside of main function
# local variable :inside the function

# global variable
# 1. it will created inside the main space
# 2.it will be accessiable in outside and inside the function
# 3. global var. can be modified in outside but not in from inside the function
# 4.to modify global var. from inside we have to use 'global' keyword , it should be in 1st line


# a = 100
# b = 200


# def sam():
#     global a,b
#     a=1000
#     b=2000
#     print("inside:", a, b)

# # a=1000
# print(" before outside:", a, b)
# sam()
# print(" after outside:", a, b)

# local variable
# 1. it will get stored inside the method area pr function area
# 2. it can not be access outside the function but cam be accessed inside the function
# 3. it can be modified inside the function but can not be modified inside the nested function and outside the main function
#4. to modified local var from inside nested function we have to used 'nonlocal' keyword, it should be written in 1st line


# def sam():
#     a = 100
#     b = 200

    # print("inside", a, b)
    # a=1000
    # print('after mod:',a,b)
    # def inner():
    #     nonlocal a,b
    #     a=1000
    #     b=2000
    #     print("nested fucntion:", a, b)
        
    # print('before',a,b)
    # inner()
    # print('after',a,b)


# sam()


# print('outside',a,b)
