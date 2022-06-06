from flask import Blueprint, render_template, request, flash, jsonify
from BACKEND import get_route_norm, oxygen_imprint, brutto, get_stations
from bs4 import BeautifulSoup as bs4

views = Blueprint('views', __name__)
stations = get_stations()
stations.remove('')

def calculate(cargo_weight, cargo_volume, start_station, end_station):
    try:
        cargo_weight = float(cargo_weight)
        cargo_volume = float(cargo_volume)
    except ValueError:
        flash('No routefrom', category='error')
        return (None, None, None)
    else:
        result = oxygen_imprint(get_route_norm(start_station, end_station, brutto(cargo_weight, cargo_volume)))
        flash('Done!', category='success')
    return (result, 45, 0)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit1':
            print(request.form.get('routefrom'))
            result, pie_procent, truck_result = calculate(request.form.get('cargowight'), request.form.get('cargovoluume'),
                               request.form.get('routefrom'), request.form.get('routeto'))
            return render_template("home.html", stations=stations, result=result, pie_procent=pie_procent, truck_result=truck_result)
        elif request.form['submit_button'] == 'submit2':
            return render_template("home.html", stations=stations)
    else:
        return render_template("home.html", stations=stations)
