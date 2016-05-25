# -*- coding: utf-8 -*-
"""
See how encode and decode works in python3.

Created on Tue May 24 23:51:01 2016

@author: ch3cooh
"""

# unicode --encode--> bytes --decode--> unicode

s1 = 'big news 搞个大新闻' # unicode by default
s2 = u'huge fortune 闷声发大财'

print(type(s1))
print(type(s2))

print('The same string in different encoding: ')
print('utf-8 : ', s1.encode('utf-8'))
print('utf-16: ',s1.encode('utf-16'))
print('utf-32: ', s1.encode('utf-32'))
print('gb2312: ', s1.encode('gb2312'))
print('gbk   : ', s1.encode('gbk'))
print('Iterate over a unicode string: ')
for c in s1:
    print(c, end='_')
print()

print('Read a unicode string from a file: ')
f = open('encoding.txt', 'w')
# f.write() only takes str as argument
f.write(s1)
f.close()
f = open('encoding.txt')
line = f.readline()
print('type of file.readline(): ')
print(type(line))   # str
