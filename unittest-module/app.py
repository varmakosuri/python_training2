class operations:
	# def __init__(self,*args,**kwargs):
	# 	self.args=args
	# 	self.context=kwargs
	def add(self,*args):
		try:
			str_check = map(lambda x: isinstance(x,str),args)
			if all(str_check):
				res=""
				for i in args:
					res=res+i 
				return res
			return sum(args)
		except:
			return None
	def prime_check(self,number):
		flag=True
		for i in range(2,number):
			if number%i==0:
				flag=False
				break
		return flag
	def mean1(self, *args):
		return mean(self.args)
	def dir_restart(self,rest,dir):
		print "erite code to restart the director"


