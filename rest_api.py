import datetime

from flask import Flask

from source.WeatherAPI.json_generator import WeatherJSONGenerator

app = Flask(__name__)


@app.route('/today')
def today_weather():
    date = datetime.datetime.now().strftime("%Y%m%d")
    return WeatherJSONGenerator.generate(date)


@app.route('/day_weather/<day>')
def day_weather(day):
    try:
        return WeatherJSONGenerator.generate(day)
    except FileNotFoundError:
        return {'message': 'There is no data for that date!'}


@app.route('/available_days')
def available_days():
    return WeatherJSONGenerator.available_dates()


if __name__ == '__main__':
    app.run(debug=False, port=80, host='0.0.0.0')
