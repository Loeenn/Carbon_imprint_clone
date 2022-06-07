from flask import Blueprint, render_template, request, flash, jsonify
from BACKEND import get_route_norm, oxygen_imprint, brutto, get_stations, truck_imprint

views = Blueprint('views', __name__)


def calculate(cargo_weight, cargo_volume, start_station, end_station):
    if "" in (cargo_weight, cargo_volume):
        result = None
        flash('No routefrom', category='error')
    else:
        fuel_summary, length_summary = get_route_norm(start_station, end_station, brutto(cargo_weight, cargo_volume))
        result = oxygen_imprint(fuel_summary)
        truck_result = truck_imprint(start_station, end_station, length_summary, cargo_weight)
        flash('Done!', category='success')
        return [result, truck_result]


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit1':
            result, truck_result = calculate(float(request.form.get('cargowight')), request.form.get('cargovoluume'),
                                             request.form.get('routefrom'), request.form.get('routeto'))
            pie_percent = round(result/truck_result*100)
            truck_result = round(truck_result)
            stations = get_stations()
            return render_template("home.html", result=result, pie_procent=pie_percent, truck_result=truck_result,
                                   stations=stations)
        elif request.form['submit_button'] == 'submit2':
            return render_template("home.html")
    else:
        stations = get_stations()
        return render_template("home.html", stations=stations)
