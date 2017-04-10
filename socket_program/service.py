import socket
import db
import json
s=""
try:
    port=8889
    host=socket.gethostname()
    s = socket.socket()
    s.bind((host,port))
    s.listen(6)
    print "waiting for the request"
    co,ci =  s.accept()
    print co,ci
    co.send("connecetion establshed")
    data_req = co.recv(1024)
    print "data_req=",data_req
    resp = db.browse_students(data_req)
    resp = json.dumps(resp)
    co.send(resp)
except Exception as err:
    print err


finally:
    if s:
        s.close()