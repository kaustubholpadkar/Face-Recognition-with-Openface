#!/usr/bin/env bash

export CONFIG_PATH='/bamos/kaustubh/Face-Recognition-with-Openface/config/config.json'
export DLIB_FACE_PREDICTOR='/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
export NETWORK_MODEL='/root/openface/models/openface/nn4.small2.v1.t7'
export IMG_DIM='96'
export THRESHOLD='.99'
export IMG_PATH='/bamos/kaustubh/Face-Recognition-with-Openface/images/test/amitabh-srk.jpg'
export LOG_LEVEL='DEBUG'
export LOG_PATH=''

python main.py
