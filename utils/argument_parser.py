import os
import argparse


class ArgumentParser():
    """
    Class to parse application arguments
    """
    def __init__(self):
        """
        Constructor to configure parser with options
        """
        self._parser = argparse.ArgumentParser(
            description="Face Recognition with Openface"
        )

        self._parser.add_argument(
            "--config_path",
            type=str,
            default=os.getenv("CONFIG_PATH", "")
        )

        self._parser.add_argument(
            "--dlib_face_predictor",
            type=str,
            default=os.getenv("DLIB_FACE_PREDICTOR", "")
        )

        self._parser.add_argument(
            "--network_model",
            type=str,
            default=os.getenv("NETWORK_MODEL", "")
        )

        self._parser.add_argument(
            "--img_dim",
            type=int,
            default=os.getenv("IMG_DIM", 96)
        )

        self._parser.add_argument(
            "--threshold",
            type=float,
            default=os.getenv("THRESHOLD", 0.5)
        )

        self._parser.add_argument(
            "--img_path",
            type=str,
            default=os.getenv("IMG_PATH", "")
        )

        self._parser.add_argument(
            '--log_level',
            type=str,
            default=os.getenv('LOG_LEVEL', 'info'),
            help='Log level.Values can be: info/debug/warning/error/critical. (default: info)'
        )

        self._parser.add_argument(
            '--log_path',
            type=str,
            default=os.getenv('LOG_PATH', ''),
            help='Log file path.'
        )

    def parse(self):
        """
        Function to parse arguments
        """
        arguments = self._parser.parse_args()
        self._validate(arguments)
        return arguments

    def _validate(self, arguments):
        """
        Function to validate arguments
        :param arguments: arguments parsed by parser
        """
        pass
