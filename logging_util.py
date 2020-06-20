import logging
import logging.config
import logging.handlers
import yaml


def init(path):
    with open(path, 'r') as f:
        try:
            log_cfg = yaml.safe_load(f.read())
        except yaml.YAMLError as err:
            print(err)

    logging.config.dictConfig(log_cfg)
    logging.getLogger(__name__).debug('Loaded Config file : "%s"', path)


def get_logger(name):
    return logging.getLogger(name)
