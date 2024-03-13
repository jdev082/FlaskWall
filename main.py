from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from Sunshine import Sunshine

s = Sunshine('database.json')

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main(name=None):
    return render_template('index.html', get_msgs = get_msgs())

def add_msg_to_db(n, c):
    o = {"name": n, "content": c}
    identifier: int = s.push(o)

def get_msgs():
    data: list[dict[str, any]] = s.all()
    return data

@app.post("/post")
def post():
    name = request.form["name"]
    content = request.form["content"]
    add_msg_to_db(name, content)
    return redirect("/", code=307)

app.run(host='0.0.0.0')
