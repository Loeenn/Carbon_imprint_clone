from flask import Blueprint, render_template, request, flash, jsonify
from BACKEND import get_route_norm, oxygen_imprint, brutto

views = Blueprint('views', __name__)


def calculate(cargo_weight, cargo_volume, start_station, end_station):
    if "" in (cargo_weight, cargo_volume):
        result = None
        flash('No routefrom', category='error')
    else:
        result = oxygen_imprint(get_route_norm(start_station, end_station, brutto(cargo_weight, cargo_volume)))
        flash('Done!', category='success')
    return result


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit1':
            result, truck_result, pie_procent = *calculate(request.form.get('cargowight'), request.form.get('cargovoluume'),
                               request.form.get('routefrom'), request.form.get('routeto'))
            return render_template("home.html", result=result, pie_procent=pie_procent, truck_result=truck_result)
        elif request.form['submit_button'] == 'submit2':
            return render_template("home.html")
    else:
        return render_template("home.html")
