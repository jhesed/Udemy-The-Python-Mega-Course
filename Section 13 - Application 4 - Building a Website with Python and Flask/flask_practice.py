"""
Udemy: The Python Mega Course:  Building 10 Real World Applications
Section 13: Application 4: Building a Website with Python and Flask

Author: Jhesed Tacadena
Date: 2017-01-30

Section 14 Contents:
  84. Demonstration of the Website
  85. Building your First Website
  86. Returning HTML Templates
  87. Adding a Navigation Menu
  88. Adding CSS Styling
  89. Creating a Python Virtual Environment
  90. Deploying the Website to a Live Server
  91. Maintaining the Website

Notes:
    * To run virtual env: `python -m venv virtual`
    * Uses Heroku as the test deployment server:
      `https://dashboard.heroku.com/`
    * Download heroku toolbelt = used to communicate with Heroku 
      via commandline: `https://devcenter.heroku.com/articles/heroku-cli`

"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

