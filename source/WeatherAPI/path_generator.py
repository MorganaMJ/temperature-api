DATA_DIR = 'data/'


class PathGenerator:
    @staticmethod
    def get_data_dir():
        return DATA_DIR

    @staticmethod
    def get_data_file_path(date):
        return DATA_DIR+str(date)+'_weather.csv'
