from flask import Blueprint, render_template, request, flash, redirect, url_for
from Backend.rail_imprint import get_route_norm, oxygen_imprint, brutto, get_stations, truck_imprint
from flask_login import login_required, current_user


views = Blueprint('views', __name__)

stations = get_stations()

stations.remove("")
typeCargo = ['Уголь', 'Щебень', 'Песок']
typePackage = ['Нет', 'Мешок']


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
@login_required
def home():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Logout':
            return redirect(url_for('auth.logout'))
        try:
            result, truck_result = calculate(float(request.form.get('cargowight')), float(request.form.get('cargovoluume')),
                                         request.form.get('routefrom'), request.form.get('routeto'), request.form.get('pacageType'), request.form.get('cargoType'))
            flash('Done!', category='success')
        except ValueError:
            flash('No routefrom', category='error')
            return render_template("home.html", stations=stations, typeCargo=typeCargo, typePackage=typePackage)
        bar_percent = 100 * max(result, truck_result) // min(result, truck_result)
        truck_result = round(truck_result)
        return render_template("home.html", result=result, bar_procent=bar_percent, truck_result=truck_result,
                               stations=stations, typeCargo=typeCargo, typePackage=typePackage, max_kakay_to_huina=max(truck_result, result))
    else:
        return render_template("home.html", stations=stations, typeCargo=typeCargo, typePackage=typePackage, user=current_user)
