from flask import Blueprint, render_template, request, flash, jsonify
import BACKEND

views = Blueprint('views', __name__)




def calculate(input_info1):
    if input_info1 == "":
        result = None
        flash('No routefrom', category='error')
    else:
        result = BACKEND.someFunc(input_info1)
        flash('Done!', category='success')
    return result


@views.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit1':
            result = calculate(request.form.get('routefrom'))
            return render_template("home.html", result=result)
        elif request.form['submit_button'] == 'submit2':
            return render_template("home.html", result=None)
        else:
            return render_template("home.html", result=None)
    else:
        return render_template("home.html", result=None)