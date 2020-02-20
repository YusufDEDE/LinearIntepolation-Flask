from flask import Flask, escape, request, render_template

app = Flask(__name__)   


def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/calc', methods=['POST', 'GET'])
def calc():


if __name__ == "__main__":
    app.run(debug=True)