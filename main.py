from flask import Flask
import random

app = Flask(__name__)


def get_number(func):
    def wrapper():
        num = random.randint(0, 10)
        return f"{num}"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1> Guess a number between 0 and 9 <h1>' \
           '<img src="https://media0.giphy.com/media/c1c75GbQdm0JGTrj5x/giphy.gif?cid=ecf05e473020c82b2072a4eea3d91ffe252803cd4364855f&rid=giphy.gif&ct=s">'


@app.route('/<int:number>')
def guessed_number(number):
    num = random.randint(0, 10)
    if number == num:
        return '<h1> CORRECT <h1>'\
                '<img src="https://media4.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif?cid=ecf05e47td1yo1ip6sr8aizleq12v3xvdwu8kw7y1pppdt60&rid=giphy.gif&ct=g">'
    elif number > num:
        return '<h1> NUMBER IS TOO HIGH <h1>'\
                '<img src="https://media4.giphy.com/media/2cei8MJiL2OWga5XoC/giphy.gif?cid=ecf05e47fgxrkhos79bslll5d0k0g9q6hbd7rs5xudfnttop&rid=giphy.gif&ct=g">'
    elif number < num:
        return '<h1> NUMER IS TOO LOW <h1>'\
                '<img src="https://media4.giphy.com/media/3osxYjAburqkbbOPeg/giphy.gif?cid=ecf05e47zyaadxqqkbeddpv7zfprur4s4q9t2lz95lin1yqw&rid=giphy.gif&ct=g">'


if __name__ == "__main__":
    app.run(debug=True)

