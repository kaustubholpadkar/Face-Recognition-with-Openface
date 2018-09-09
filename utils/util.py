import json


def parse_config(config_path):
    """
    Function to load json configuration file
    :return: dict loaded from json
    """
    try:
        with open(config_path) as json_config:
                return json.load(json_config)
    except FileNotFoundError:
        raise FileNotFoundError("Configuration File {} not Found".format(config_path))
    except FileExistsError:
        raise FileNotFoundError("Configuration File {} does not Exist".format(config_path))
    except json.JSONDecodeError as jsonerror:
        raise jsonerror("The config file at {} is formatted incorrectly".format(config_path))
    except Exception as e:
        raise Exception("Exception {} in loading Configuration File {}".format(e, config_path))
