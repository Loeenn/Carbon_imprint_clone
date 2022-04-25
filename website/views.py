from flask import Blueprint, render_template, request, flash, jsonify
import BACKEND

views = Blueprint('views', __name__)




def calculate(cargowight, cargovoluume):
    if "" in (cargowight, cargovoluume):
        result = None
        flash('No routefrom', category='error')
    else:
        result = BACKEND.brutto(cargowight, cargovoluume)
        flash('Done!', category='success')
    return result


@views.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit1':
            result = calculate(request.form.get('cargowight'), request.form.get('cargovoluume'))
            return render_template("home.html", result=result)
        elif request.form['submit_button'] == 'submit2':
            return render_template("home.html", result=None)
        else:
            return render_template("home.html", result=None)
    else:
        return render_template("home.html", result=None)