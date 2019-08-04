import datetime
import random
import time


class WeatherData:
    def __init__(self, temperature, humidity, reading_date):
        self.temperature = temperature
        self.humidity = humidity
        self.reading_date = reading_date

    def get_csv_row(self):
        return self.reading_date+','+str(self.temperature)[:4]+','+str(self.humidity)[:4]+'\n'


class WeatherReader:

    def __init__(self, sensor_pin=22):
        self.sensor_pin = sensor_pin

    def get_weather_data(self, random_data=False):
        if random_data:
            return self._get_random_data()
        else:
            return self._get_sensor_data()

    @staticmethod
    def _get_random_data():
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        mock_temperature = random.randint(-10, 40)
        mock_humidity = random.randint(10, 90)
        return WeatherData(mock_temperature, mock_humidity, date_now)

    def _get_sensor_data(self):
        import Adafruit_DHT
        sensor = Adafruit_DHT.DHT22
        humidity, temperature = Adafruit_DHT.read_retry(sensor, self.sensor_pin)
        date_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return WeatherData(temperature, humidity, date_now)


class WeatherWriter:
    @staticmethod
    def write(weather_data):
        filename = WeatherWriter._get_file_name()
        with open('data/'+filename, 'a') as f:
            f.write(weather_data.get_csv_row())

    @staticmethod
    def _get_file_name():
        date = datetime.datetime.now().strftime("%Y%m%d")
        return date+'_weather.csv'


while True:
    reader = WeatherReader()
    current_data = reader.get_weather_data(random_data=True)
    WeatherWriter.write(current_data)
    time.sleep(3600)
