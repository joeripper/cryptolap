from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return('fuck')

if__name__ == '__main__':
	app.run(port=5000, debug=True)