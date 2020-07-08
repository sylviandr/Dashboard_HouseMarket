from flask import Flask, render_template
import plotly
import plotly.graph_objects as go
import chart_studio.plotly as csp
import json

app = Flask(__name__)

# @app.route('/') #home
# def home():
#     return 'Hello, Jakarta'

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/about')#about
# def about():
#     return 'Selamat Belajar Data Science'

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')


if __name__ =='__main__':
    app.run(debug=True)

# , methods=['POST', 'GET']