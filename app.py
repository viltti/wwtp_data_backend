from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from config import get_config
from services import get_variables, get_history_data, get_daily_data, get_hourly_data
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config.update(get_config())
config_dict = get_config()
app.config.update(config_dict)
auth = HTTPBasicAuth()

users = {
    config_dict['BASIC_AUTH_USERNAME']: generate_password_hash(config_dict['BASIC_AUTH_PASSWORD'])
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/api/variables')
def variables():
    data = get_variables()
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch variables data"}), 500
    
@app.route('/api/data/history')
def get_all_history_data():
    data = get_history_data(None)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch history data"}), 500
    
@app.route('/api/data/variable/<variable>/history')
def history_data(variable):
    data = get_history_data(variable)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch history data"}), 500
    
@app.route('/api/data/variable/<variable>/day')
def day_data(variable):
    print('variable day_data', variable)
    data = get_daily_data(variable)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch day data"}), 500
    
@app.route('/api/data/variable/<variable>/hour')
def hour_data(variable):
    data = get_hourly_data(variable)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Unable to fetch hour data"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port, debug=False)