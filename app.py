import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	return 'So sorry I haven\'t made a main page yet.... but Hello World! :D \nOnly the other links work ex. something.com/test'

@app.route('/dino')
def dinosaur():
	return 'Dinosaur'

@app.route('/sigma')
def sig():
	#import scraper
	#scraper.make_graph()
	return render_template('cat.html',name='MALgraph.gexf')

@app.route('/college')

@app.route('/css/<path:fn>')
def css_static(fn):
	return send_from_directory('/css/',fn)

@app.route('/js/<path:fn>')
def js_static(fn):
	return send_from_directory(app.config['JS_STATIC'],fn)



@app.route('/temp/<name>')
def temp(name=None):
	return render_template('display.html',name=name)

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000
	port = int(os.environ.get('PORT',5000))
	app.run(host='0.0.0.0',port=port,debug=True)
