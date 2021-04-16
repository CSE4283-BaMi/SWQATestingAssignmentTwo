from flask import Flask, render_template, request
import math
from assignmentTwo import *

app = Flask(__name__)

def calc_bmi(weight, heightFT, heightIN):
    data = (weight, heightFT, heightIN)
    result = bmi(data, True)
    return result

def calc_retirement(age, salary, percentSaved, goal):
    data = (age, salary, percentSaved, goal)
    result = retirement(data, True)
    return result
    

@app.route("/", methods = ['GET', 'POST'])
def index3():
    return render_template("index.html")

@app.route("/bmi", methods = ['GET', 'POST'])
def index():
    bmi = ''

    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        heightFT = float(request.form.get('heightFT'))
        heightIN = float(request.form.get('heightIN'))
        bmi = calc_bmi(weight, heightFT, heightIN)

    return render_template("bmi_calc.html", bmi = bmi)

@app.route("/retirement", methods = ['GET', 'POST'])
def index2():
    retirement = ''

    if request.method == 'POST' in request.form:
        age = int(request.form.get('age'))
        salary = float(request.form.get('salary'))
        percentSaved = float(request.form.get('percentSaved'))
        goal = float(request.form.get('goal'))
        retirement = calc_retirement(age, salary, percentSaved, goal)

    return render_template("retirement_calc.html", retirement = retirement)



if __name__ == "__main__":
    app.run()

