from utils.util import parse_config
from utils.openface_utility import OpenfaceUtil


class FaceRecognizer():
    """
    Class for Face Recognition
    """
    def __init__(self, config,
                 dlib_face_predictor="shape_predictor_68_face_landmarks.dat",
                 network_model="nn4.small2.v1.t7",
                 img_dim=96, threshold=0.5):
        self._openface_util = OpenfaceUtil(dlib_face_predictor, network_model, img_dim)
        self.threshold = threshold
        self.configuration = parse_config(config)
        self._compute_representation()

    def _compute_representation(self):
        for config in self.configuration:
            config["representation"] = self._openface_util.get_representation(config["path"])

    def recognize(self, path):
        rep = self._openface_util.get_representation(path)
        min_distance = self.threshold
        recognized_name = None
        for config in self.configuration:
            distance = OpenfaceUtil.get_distance(rep, config["representation"])
            if distance <= min_distance:
                min_distance = distance
                recognized_name = config["name"]
        return recognized_name