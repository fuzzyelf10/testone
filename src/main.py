from flask import Flask

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
	return '329d4feb-c5c0-4de5-b10c-701b44fbec4f'

if __name__ == '__main__':
	app.run(host='0.0.0.0')