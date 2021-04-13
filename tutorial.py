from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

def calc_retirement(age, salary, percSaved, goal):
    empMatch = .35
    #ageCap = 100

    salaryPercent = salary * percSaved
    empPercent = salaryPercent * empMatch
    saveInstallment = salaryPercent * empPercent
    amountYears = math.ceil(goal / saveInstallment)
    endAge = age + amountYears
    return endAge

@app.route("/")
def index3():
    return render_template("index.html")

@app.route("/bmi", methods = ['GET', 'POST'])
def index():
    bmi = ''

    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)

    return render_template("bmi_calc.html", bmi = bmi)

@app.route("/retirement", methods = ['GET', 'POST'])
def index2():
    retirement = ''

    if request.method == 'POST' in request.form:
        age = int(request.form.get('age'))
        salary = float(request.form.get('salary'))
        percSaved = float(request.form.get('percSaved'))
        goal = float(request.form.get('goal'))
        retirement = calc_retirement(age, salary, percSaved, goal)

    return render_template("retirement_calc.html", retirement = retirement)



if __name__ == "__main__":
    app.run()

