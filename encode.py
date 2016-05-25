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

# Output
"""
<class 'str'>
<class 'str'>
The same string in different encoding: 
utf-8 :  b'big news \xe6\x90\x9e\xe4\xb8\xaa\xe5\xa4\xa7\xe6\x96\xb0\xe9\x97\xbb'
utf-16:  b"\xff\xfeb\x00i\x00g\x00 \x00n\x00e\x00w\x00s\x00 \x00\x1ed*N'Y\xb0e\xfb\x95"
utf-32:  b"\xff\xfe\x00\x00b\x00\x00\x00i\x00\x00\x00g\x00\x00\x00 \x00\x00\x00n\x00\x00\x00e\x00\x00\x00w\x00\x00\x00s\x00\x00\x00 \x00\x00\x00\x1ed\x00\x00*N\x00\x00'Y\x00\x00\xb0e\x00\x00\xfb\x95\x00\x00"
gb2312:  b'big news \xb8\xe3\xb8\xf6\xb4\xf3\xd0\xc2\xce\xc5'
gbk   :  b'big news \xb8\xe3\xb8\xf6\xb4\xf3\xd0\xc2\xce\xc5'
Iterate over a unicode string: 
b_i_g_ _n_e_w_s_ _搞_个_大_新_闻_
Read a unicode string from a file: 
type of file.readline(): 
<class 'str'>
"""
