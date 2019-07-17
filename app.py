from aiohttp import web
import logging
from PIL import ImageFile
import yaml
from lib.app import NSFWApp

with open('config.yaml') as config_definition:
    config = yaml.safe_load(config_definition)

    if config and config['logging'] and config['logging']['level']:
        log_level = 'WARNING'
    else:
        log_level = config['logging']['level'].upper()


logging.basicConfig(level=log_level)

ImageFile.LOAD_TRUNCATED_IMAGES = True

web.run_app(NSFWApp(config))
