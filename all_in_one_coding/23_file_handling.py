'''
file: file is a container which is used to store the data/instructins.
eg. extension are .docx,.html,.py,.json,.java
by looking into extension , user can identify what type of data is store.

operation on file:


path:It is the location where the file is present in the system.
C:\Users\KIIT01\Desktop\package_arch
window:back-slash is used: it is run by using DOS(disk operating system)
linux/max:forward-slah

back-slash escape sequence problem:
\-->escape sequence char
# print('c:\newfolder')
OS:operating system
import os
path=os.path.join('c:','user','hp','desktop','newfolder')
# output:c:\users\hp\desktop\newfolder
print('sepe',os.sep)

#file operation:
1.Back-slash escape sequence problem
#window:(\ because it work on DOS(disk operating system))
linux/mac: forward-slash

path:
# print('c\:newfolder')
import os 
# path=os.path.join('c:',os.sep,'user','desktop','newfolder')
path=os.path.join(r'C:\Users\KIIT01\Desktop\file_operation')
print('path',path)
print('separator',os.sep)
two types of path:
1.absolute path:it is the full path from the root of the system
eg: C:\Users\KIIT01\Desktop\file_operation
2.relative path:path relative to current working directory
eg : file_operation\data.txt
os.getcwd()
cwd-->current working directory

import os
print('current working directory is:',os.getcwd())


to check whether the path is absolute or not
# os.path.isabs(path):absolute path->true, relative path--->false

import os 
path=os.path.join(r'C:\Users\KIIT01\Desktop\file_operation')
print('is absolute path:',os.path.isabs(path))


#converting relative path into absolute path
os.path.abspath(path)
eg:
import os 
path=os.path.join('data.txt')
print('absolute path is :',os.path.abspath(path))
file operation:

i.finding the file sizes and folder contents:
file size:

ii.copying and moving files 
iii.open(),read(),write(),append()--->txt,cvs




'''