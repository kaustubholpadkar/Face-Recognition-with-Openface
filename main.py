import logging
from utils.argument_parser import ArgumentParser
from facerecognition.facerecognizer import FaceRecognizer


def main():
    try:
        parser = ArgumentParser()
        arguments = parser.parse()
        if arguments.log_path:
            logging.basicConfig(filename=arguments.log_path, level=arguments.log_level)
        else:
            logging.basicConfig(level=arguments.log_level)

        face_recognizer = FaceRecognizer(arguments.config_path,
                                         arguments.dlib_face_predictor,
                                         arguments.network_model,
                                         arguments.img_dim,
                                         arguments.threshold)
        recognition_result = face_recognizer.recognize(arguments.img_path)
        logging.info("Result : {}".format(recognition_result))
    except Exception as e:
        logging.error("Error encountered during execution: {}".format(e))


if __name__ == '__main__':
    main()
