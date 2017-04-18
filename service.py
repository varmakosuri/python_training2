from flask import Flask
import json
app = Flask(__name__)

@app.route('/luns')
def get_luns():
	return json.dumps([{'id':1,"name":"name1"},{'id':2,"name":"name2"}])

@app.route('/iniatorgroups')
def get_iniatorgroups():
	return json.dumps([{'id':1,"name":"group1"},{'id':2,"name":"group2"}])

if __name__ == "__main__":
	app.run(port=9999)