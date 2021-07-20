
#Charlene Crystal Namuyige 
#7/19/2021
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/about")
def second_page():
    return render_template('about.html', subtitle='About Page', text='This is the about page')
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
