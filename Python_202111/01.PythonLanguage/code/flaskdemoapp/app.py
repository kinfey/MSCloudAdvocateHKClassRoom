from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/about')
def about():
    return '關於Reactor'

@app.route('/info/<name>')
def get_name(name):
  return '你好 ' + str(name)

@app.route('/info2')
def get_name2():
  name = request.args.get('name')
  return '你好 ' + str(name)

@app.route('/info3', methods=['POST'])
def get_name3():
    
  name = request.form.get('name')
  return '你好 ' + str(name)



@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/index2')
def index2():
    message = {
        'enName':'kinfey',
        'chName':'建暉'
    }
    return render_template('index2.html', info = message)