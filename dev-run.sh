#!/usr/bin/env bash

export CONFIG_PATH='/bamos/kaustubh/Face-Recognition-with-Openface/config/config.json'
export DLIB_FACE_PREDICTOR='/root/openface/models/dlib/shape_predictor_68_face_landmarks.dat'
export NETWORK_MODEL='/root/openface/models/openface/nn4.small2.v1.t7'
export IMG_DIM='96'
export THRESHOLD='0.5'
export IMG_PATH='/bamos/kaustubh/Face-Recognition-with-Openface/images/test/rajkumar2.jpg'
export LOG_LEVEL='INFO'
export LOG_PATH=''

python main.py
