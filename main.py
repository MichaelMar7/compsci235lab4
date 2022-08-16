from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")
    #return "<h1> Hello world </h1>"

@app.route("/user/<username>")
def show_user_profile(username):
    '''Beware URL encoding. eg., "Hello World" becomes "Hello%20Wold" '''
    return f'User {escape(username)}'

@app.route("/result/<mark>")
def show_mark(mark):
    mark = int(mark)
    if mark >= 90:
        grade = 'A+' 
    elif mark < 90 and mark >= 85:
        grade = 'A'
    elif mark < 85 and mark >= 80:
        grade = 'A-'
    elif mark < 80 and mark >= 75:
        grade = 'B+'
    elif mark < 75 and mark >= 70:
        grade = 'B'
    elif mark < 70 and mark >= 65:
        grade = 'B-'
    elif mark < 65 and mark >= 60:
        grade = 'C+'
    elif mark < 60 and mark >= 55:
        grade = 'C'
    elif mark < 55 and mark >= 50:
        grade = 'C-'
    elif mark < 50 and mark >= 45:
        grade = 'D+'
    elif mark < 45 and mark >= 40:
        grade = 'D'
    elif mark < 40:
        grade = 'D-'
    return f'Grade {grade}'

if __name__ == "__main__":
    app.run(debug=True,port=8000)
