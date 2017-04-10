import socket
s=""
try:
    port=8889
    host=socket.gethostname()
    s = socket.socket()
    s.connect((host,port))
    ack = s.recv(1024)
    print ack
    a=raw_input("Enter id:")
    s.send(a)
    resp=s.recv(1024)
    print "response=",resp
except Exception as err:
    print err
finally:
    if s:
        s.close()