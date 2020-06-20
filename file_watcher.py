import time
import shutil
import os
import logging_util
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from config_reader import ConfigOptions


class Event(LoggingEventHandler):
    def on_created(self, event):
        move_file()


def move_file():
    files = os.listdir(source_path)
    for file in files:
        logger.info('Moving file : %s', source_path + file)
        shutil.move(source_path + file, determine_category_path(file))


def determine_category_path(file_name):
    determined_category = 'other'
    for classification in file_classification.keys():
        for file_type in file_classification[classification]:
            if file_type.lower() == file_name.split('.')[1].lower():
                determined_category = classification
                break

    determined_path = destination_path + determined_category

    return determined_path


def check_and_create_folders():
    for dir_name in dir_categories:
        final_dir = destination_path + dir_name

        if not os.path.isdir(final_dir):
            os.mkdir(final_dir)
            logger.debug('Created directory : %s', final_dir)
        else:
            logger.debug('Directory %s already exists', final_dir)


def start_watching():
    event_handler = Event()
    observer = Observer()
    observer.schedule(event_handler, source_path, recursive=True)
    observer.start()

    logger.info('Started Monitoring')
    check_and_create_folders()
    move_file()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


config_options = ConfigOptions()
destination_path = config_options.get_destination_path()
source_path = config_options.get_source_path()
dir_categories = config_options.get_categories()
file_classification = dict(config_options.get_file_classification())

logging_util.init(config_options.get_log_config_file())
logger = logging_util.get_logger(__name__)

start_watching()
