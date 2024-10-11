from flask import Flask, jsonify

app = Flask(__name__)

# Dummy weather data for the '/weather' endpoint
weather_data = {
    "city": "New York",
    "temperature": "22°C",
    "description": "Partly cloudy"
}

# Dummy forecast data for the '/forecast' endpoint
forecast_data = {
    "city": "New York",
    "forecast": [
        {"day": "Monday", "temperature": "21°C", "description": "Cloudy"},
        {"day": "Tuesday", "temperature": "23°C", "description": "Sunny"},
        {"day": "Wednesday", "temperature": "19°C", "description": "Rainy"}
    ]
}

# Weather endpoint
@app.route('/weather', methods=['GET'])
def get_weather():
    return jsonify(weather_data)

# Forecast endpoint
@app.route('/forecast', methods=['GET'])
def get_forecast():
    return jsonify(forecast_data)

if __name__ == '__main__':
    app.run(debug=True)
