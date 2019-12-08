import logging
from utils.argument_parser import ArgumentParser
from facerecognition.facerecognizer import FaceRecognizer


def main():
    """
    Function to start Application
    :return:
    """
    try:
        # Parse Application Arguments
        parser = ArgumentParser()
        arguments = parser.parse()

        # Set Logging Configurations
        if arguments.log_path:
            logging.basicConfig(filename=arguments.log_path, level=arguments.log_level.upper())
        else:
            logging.basicConfig(level=arguments.log_level.upper())

        logging.debug("Arguments: {}".format(arguments))

        # Create FaceRecognizer object
        face_recognizer = FaceRecognizer(arguments.config_path,
                                         arguments.dlib_face_predictor,
                                         arguments.network_model,
                                         arguments.img_dim,
                                         arguments.threshold)

        # Recognize the Face
        recognition_result = face_recognizer.recognize(arguments.img_path)
        logging.info("Result : {}".format(recognition_result))
    except Exception as e:
        logging.error("Error encountered during execution: {}".format(e))


if __name__ == '__main__':
    main()
