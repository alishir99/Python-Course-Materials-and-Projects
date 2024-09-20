import time

from flask import Flask

app = Flask(__name__)

@app.route("/")   # decorator
def hello_world():
    return '<h1 style = "text-align: center "> مونون کاندوم کلان دوست داره</h1>' \
           '<img src="https://media4.giphy.com/media/125cGBp1PjTNCM/200w.webp?' \
           'cid=ecf05e479mj7n5i70b84c7kpn2hiticav6trgkxnw62rk9vw&ep=v1_gifs_search&rid=200w.' \
           'webp&ct=g"width = 1200, text-align : center>'
def make_bold(function):
    def wrapper_function():

        return f"<b>" + function()+ "</b>"
    return wrapper_function

def make_center(function):
    def wrapper():
        return  '<h1 style = "text-align: center">' + function()
    return wrapper()

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper
def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route("/<name>")

def what_is_your_name(name):
    return f"Hello {name}!"
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

if __name__ == "__main__":
    app.run(debug=True)