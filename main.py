from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Main Page'

@app.route('/api1')
def api1():
	res1 = requests.get('http://api1-svc')
	return res1.text

@app.route('/api2')
def api2():
	res2 = requests.get('http://api2-svc')
	return res2.text

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port="8000")
