from flask import Blueprint, render_template, request, flash, jsonify
from BACKEND import get_route_norm, oxygen_imprint, brutto, get_stations, truck_imprint

views = Blueprint('views', __name__)

stations = get_stations()

stations.remove("")
typeCargo=['Уголь', 'Щебень', 'Песок']
typePackage=['Нет', 'Мешок']


def calculate(cargo_weight, cargo_volume, start_station, end_station, package_type, cargo_type):
    fuel_summary, length_summary = get_route_norm(start_station, end_station, brutto(cargo_weight, cargo_volume))
    result = oxygen_imprint(fuel_summary)
    truck_result = truck_imprint(start_station, end_station, length_summary, cargo_weight)
    flash('Done!', category='success')
    return [result, truck_result]


    # if None in (cargo_weight, cargo_volume):
    #     result = None
    #     flash('No routefrom', category='error')
    # else:
    #     cargo_weight, cargo_volume = float(cargo_weight), float(cargo_volume)
    #     fuel_summary, length_summary = get_route_norm(start_station, end_station, brutto(cargo_weight,
    #                                                                                      cargo_volume))
    #     result = oxygen_imprint(fuel_summary)
    #     truck_result = truck_imprint(start_station, end_station, length_summary, cargo_weight)
    #     flash('Done!', category='success')
    #     return [result, truck_result]


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'submit1':
            try:
                result, truck_result = calculate(float(request.form.get('cargowight')), float(request.form.get('cargovoluume')),
                                             request.form.get('routefrom'), request.form.get('routeto'), request.form.get('pacageType'), request.form.get('cargoType'))
                flash('Done!', category='success')
            except ValueError:
                flash('No routefrom', category='error')
                return render_template("home.html", stations=stations, typeCargo=typeCargo, typePackage=typePackage)
            pie_percent = round(result/truck_result*100)
            truck_result = round(truck_result)
            return render_template("home.html", result=result, pie_procent=pie_percent, truck_result=truck_result,
                                   stations=stations, typeCargo=typeCargo, typePackage=typePackage)
    else:
        return render_template("home.html", stations=stations, typeCargo=typeCargo, typePackage=typePackage)
