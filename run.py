import os

from flask import Flask, request, redirect
import retaliation

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/right/", methods=["GET"])
def move_right():
  amount = request.args["amount"]
  retaliation.main(['', 'right', amount])
  return "OK"

@app.route("/left/", methods=["GET"])
def move_left():
  amount = request.args["amount"]
  retaliation.main(['', 'left', amount])
  return "OK"

@app.route("/up/", methods=["GET"])
def move_up():
  amount = request.args["amount"]
  retaliation.main(['', 'up', amount])
  return "OK"

@app.route("/down/", methods=["GET"])
def move_down():
  amount = request.args["amount"]
  retaliation.main(['', 'down', amount])
  return "OK"

@app.route("/fire/", methods=["GET"])
def fire():
  retaliation.main(['', 'fire'])
  return "OK"

@app.route("/reset/", methods=["GET"])
def reset():
  retaliation.main(['', 'reset'])
  return "OK"

if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')
