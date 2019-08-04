import csv
import os

from .path_generator import PathGenerator


class WeatherData:
    def __init__(self, temperature, humidity, reading_date):
        self.temperature = temperature
        self.humidity = humidity
        self.reading_date = reading_date


class WeatherCSVLoader:
    @staticmethod
    def load(path):
        result_data = []
        with open(path, 'r') as weather_data_file:
            csv_reader = csv.reader(weather_data_file)
            for row in csv_reader:
                result_data.append(WeatherData(reading_date=row[0], temperature=row[1], humidity=row[2]))
        return result_data


class WeatherJSONGenerator:
    @staticmethod
    def generate(date):
        path = PathGenerator.get_data_file_path(date)
        loaded_data = WeatherCSVLoader.load(path)
        loaded_data_as_dict = {}
        list_of_data = []
        for data in loaded_data:
            list_of_data.append(data.__dict__)
        loaded_data_as_dict[date] = list_of_data
        return loaded_data_as_dict

    @staticmethod
    def available_dates():
        available_dates = {}
        list_of_dates = []
        path = PathGenerator.get_data_dir()
        for name in os.listdir(path):
            if '.csv' in name:
                list_of_dates.append(name[0:8])
        available_dates['days'] = sorted(list_of_dates)
        return available_dates
