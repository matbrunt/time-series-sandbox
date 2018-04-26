import os
import yaml
from configparser import ConfigParser


def read_config():
    config_path = os.path.abspath(os.path.join(__file__, os.pardir, 'config.yaml'))
    config = yaml.load(open(config_path))
    
    # Override config setting with environment variable, if it exists
    env_config = os.getenv('DEBUG', None)
    if env_config is not None:
        config['debug'] = env_config.lower() == 'true'

    return config


def read_credentials(section=None):
    credentials_path = os.path.abspath(os.path.join(__file__, os.pardir, 'credentials.txt'))
    credentials = ConfigParser(interpolation=None)
    credentials.read(credentials_path)

    if section is None:
        return credentials
    return credentials[section]
