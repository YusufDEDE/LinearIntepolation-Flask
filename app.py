from flask import Flask, escape, request, render_template
from LinearInterpolation import start

app = Flask(__name__)   


def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/calc', methods=['POST', 'GET'])
def calc():
    
    if request.method == 'POST':
        y0 = request.form.get('y0')
        x = request.form.get('x')
        x0 = request.form.get('x0')
        y1 = request.form.get('y1')
        x1 = request.form.get('x1')

        # start(y0, x, x0, x1, y1):
        print(start(int(y0), int(x), int(x0), int(x1), int(y1) ))
        return render_template('index.html', result=start(int(y0), int(x), int(x0), int(x1), int(y1)))
    else:
        return render_template('index.html', result="değerleri gir!")
    
    

if __name__ == "__main__":
    app.run(debug=True)