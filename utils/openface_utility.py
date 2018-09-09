import numpy as np
import cv2
np.set_printoptions(precision=2)
import openface


class OpenfaceUtil():
    """
    Class for Openface Utility
    """
    def __init__(self, dlib_face_predictor, network_model, img_dim):
        self._img_dim = img_dim
        self._align = openface.AlignDlib(dlib_face_predictor)
        self._net = openface.TorchNeuralNet(network_model, self._img_dim)

    def get_representation(self, path):
        bgr_img = cv2.imread(path)
        rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
        bb = self._align.getLargestFaceBoundingBox(rgb_img)
        aligned_face = self._align.align(self._img_dim, rgb_img, bb,
                                         landmarkIndices=openface.AlignDlib.OUTER_EYES_AND_NOSE)
        representation = self._net.forward(aligned_face)
        return representation

    @staticmethod
    def get_distance(rep1, rep2):
        distance = rep1 - rep2
        return np.dot(distance, distance)
