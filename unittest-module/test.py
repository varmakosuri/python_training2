# add unittest cases
'''
case1: 10,20 ->30
case2: str1,str2->str1str2
case3: str1,10-> None
'''
import app

o1=app.operations(10,20)
e_o1=30
a_o1=o1.add()
if e_o1 == a_o1:
	print "10,20 test case passed"
else:
	print "10,20 test case failed"