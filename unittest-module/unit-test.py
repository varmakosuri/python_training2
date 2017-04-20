import unittest
import app

class Testcaseses(unittest.TestCase):
	# @classmethod
	# def setUpClass(cls):
	# 	print "login to vplex and get the rest instance"
	# 	cls.rest=app.operations(10,20)

	# def setUp(self):
	# 	print "pre configuration for every test case"
	# 	dirs=['dir1-A','dir1-B','dir2-A']
	# def test_dir_reatrt(self):
	# 	print "call dir restrt method and check in vplex whether restrted or not"

	# def test_dir_abort(self):
	# 	print "call dir abort method and check whether dir aborted or not in vplex"
	# def tearDown(self):
	# 	print "post operation test case"
	# def
	# @classmethod
	# def tearDownClass(cls):
	# 	print "logout from the system"
	@classmethod
	def setUpClass(cls):
		cls.inst = app.operations()
	def statrt_io():
		pass
	def dir_reatrt(self):
		pass
	def test_dir_restart(self):
		pass
		# craeate threads to call io and director restart.
	def test_add_10_20(self):
		exp=30
		act=self.inst.add(10,20)
		error="10,20, test case for add operation is failed"
		self.assertEqual(exp,act,error)
	def test_add_str1_str2(self):
		exp="str1str2"
		act=self.inst.add("str1","str2")
		error="str1,str2, test case for add operation is failed"
		self.assertEqual(exp,act,error)
	def test_add_str1_10(self):
		exp=None
		act=self.inst.add("str1",10)
		error="str1, 10, test case for add operation is failed"
		self.assertEqual(exp,act,error)
	def test_prime_3(self):
		print "3 test case for prime executed"
		self.as1=20
		exp=True
		act=self.inst.prime_check(3)
		error="3 for prime test case failed"
		self.assertEqual(exp,act,error)
	def test_prime_4(self):
		print "as======",self.as1
		exp=False
		act=self.inst.prime_check(4)
		error="4 for prime test case failed"
		self.assertEqual(exp,act,error)
	@classmethod
	def tearDownclass(cls):
		cls.inst=None

if __name__ == "__main__":
	unittest.main()