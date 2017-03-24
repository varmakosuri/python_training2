"""
import a
print a.fun()
"""
'''
import mod1
print mod1.__file__
print mod1.file1.fun()
'''
'''
from mod1 import file1
print file1.fun()
'''
'''
from mod1 import file1,file2
print file1.fun()
print file2.fun()
'''
'''
import mod1
print mod1.file1.fun()
print mod1.file2.fun()
'''
"""
from mod1 import file1
"""