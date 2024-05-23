from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

sensor_data = {
    "vibration": 0,
    "noise": 0
}

@app.route('/data', methods=['POST'])
def receive_data():
    global sensor_data
    sensor_data = request.get_json()
    return jsonify({"status": "success"}), 200

@app.route('/')
def index():
    return render_template('dashboard.html', data=sensor_data)

@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
