from flask import Flask, render_template, current_app as app

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to Isabella's rainbow project"

@app.route('/red')
def red():
    color = 'red'
    return render_template('index.html', color = color)

@app.route('/orange')
def orange():
    color = 'orange'
    return render_template('index.html', color = color)

@app.route('/yellow')
def yellow():
    color = 'yellow'
    return render_template('index.html', color = color)

@app.route('/green')
def green():
    color = 'green'
    return render_template('index.html', color = color)

@app.route('/blue')
def blue():
    color = 'blue'
    return render_template('index.html', color = color)

@app.route('/indigo')
def indigo():
    color = 'indigo'
    return render_template('index.html', color = color)

@app.route('/violet')
def violet():
    color = 'violet'
    return render_template('index.html', color = color)

@app.route('/rainbow')
def rainbow():
    links = ['http://0.0.0.0:5000/red', 'http://0.0.0.0:5000/orange', 'http://0.0.0.0:5000/yellow', 'http://0.0.0.0:5000/green', 'http://0.0.0.0:5000/blue', 'http://0.0.0.0:5000/indigo', 'http://0.0.0.0:5000/violet']
    return render_template('rainbow.html', links = links)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')