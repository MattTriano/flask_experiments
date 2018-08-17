from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {}!</h1>'.format(name)

# This allows us to start this program at the command line 
# via the command 
# >python hello.py
if __name__ == '__main__':
	app.run()