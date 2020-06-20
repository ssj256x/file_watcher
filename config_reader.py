import yaml


class ConfigOptions:

    def __init__(self):
        self.__destination_path = None
        self.__log_path = None
        self.__categories = None
        self.__source_path = None
        self.__file_classification = None
        self.__log_config_file = None
        self.read_config()

    def read_config(self):
        with open('config/config.yml', 'r') as stream:
            try:
                loaded_yaml = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print(err)

        self.__log_path = str(loaded_yaml['config']['dir']['log_path'])
        self.__destination_path = str(loaded_yaml['config']['dir']['destination_path'])
        self.__categories = loaded_yaml['config']['dir']['categories']
        self.__source_path = str(loaded_yaml['config']['dir']['source_path'])
        self.__file_classification = loaded_yaml['config']['file_classification']
        self.__log_config_file = str(loaded_yaml['config']['dir']['log_config_file'])

    def get_destination_path(self):
        return self.__destination_path

    def get_log_path(self):
        return self.__log_path

    def get_categories(self):
        return self.__categories

    def get_source_path(self):
        return self.__source_path

    def get_file_classification(self):
        return self.__file_classification

    def get_log_config_file(self):
        return self.__log_config_file