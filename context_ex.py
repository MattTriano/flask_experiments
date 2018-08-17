from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is {}'.format(user_agent)

# This allows us to start this program at the command line 
# via the command 
# >python hello.py
if __name__ == '__main__':
	app.run()