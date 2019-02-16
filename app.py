from flask import Flask, render_template
import os
import sys
from flask import request
from flask import send_file

app = Flask(__name__)

@app.route('/')
def home():
    return send_file('test.pdf', as_attachment=True)



if __name__ == "__main__":
    app.run()
