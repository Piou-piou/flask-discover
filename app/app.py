from flask import Flask
from database.DatabaseConnection import DatabaseConnection
from invoice.routes import invoice_bp

app = Flask(__name__)

app.register_blueprint(invoice_bp)

@app.route('/')
def hello():
	return "Hello world"

@app.route('/<name>')
def helloName(name):
	return "Hello "+name

@app.route('/post/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
    return f'Post {post_id}'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
