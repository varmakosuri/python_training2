import logging
import app1
#result = app1.fun()
#print "program started"
logging.basicConfig(filename="log2.txt", level=logging.DEBUG,
format="%(asctime)s->%(levelname)s->%(message)s")
logging.info("program started")
a=raw_input("Enter a values:")
b=raw_input("Enter b value:")
logging.info("a={0}".format(a))
logging.info("b={0}".format(b))
if not a.isdigit() or not b.isdigit():
	logging.warn("Got the alphanumeric number may raise an exception")
a=int(a)
b=int(b)
res=a/b
logging.debug("result={0}".format(res))
#print "result",res
logging.info("other statments in program")
logging.info("program ended")
#print "other statments in program"
#print "program ended"