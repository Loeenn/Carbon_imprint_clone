from flask import Blueprint, render_template, request, flash, jsonify
from BACKEND import get_route_norm, oxygen_imprint, brutto, get_stations

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
            result = calculate(request.form.get('cargowight'), request.form.get('cargovoluume'),
                               request.form.get('routefrom'), request.form.get('routeto'))
            pie_percent = 45
            truck_result = None
            stations = get_stations()
            return render_template("home.html", result=result, pie_procent=pie_percent, truck_result=truck_result,
                                   stations=stations)
        elif request.form['submit_button'] == 'submit2':
            return render_template("home.html")
    else:
        stations = get_stations()
        return render_template("home.html", stations=stations)
