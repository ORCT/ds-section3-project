from flask import Blueprint, render_template, request
import pickle

result_bp = Blueprint('result', __name__, url_prefix='/result')

@result_bp.route('/', methods=['GET','POST'])
def result_url():
    drift = request.form.get('drift')
    accel = request.form.get('accel')
    corner = request.form.get('corner')
    boost_time = request.form.get('boost_time')
    boost_charge = request.form.get('boost_charge')
    
    X_test = [int(drift), int(accel), int(corner), int(boost_time), int(boost_charge)]
    
    with open('./model.pkl', 'rb') as pickle_file:
        model = pickle.load(pickle_file)
        X_test=[X_test]
        pred = model.predict(X_test)

    return render_template('result.html', result=pred)