import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'Hello World!'

@app.route('/dino')
def dinosaur():
	return 'Dinosaur'

@app.route('/sigma')
def sig():
	return render_template('cat.html')

@app.route('/temp/<name>')
def temp(name=None):
	return render_template('display.html',name=name)

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0',port=port)
