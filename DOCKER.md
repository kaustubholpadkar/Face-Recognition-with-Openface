# Face-Recognition-with-Openface
Face Recognition Application with Openface

#### Setup
##### How to Create Docker Image
- docker pull bamos/openface

##### How to run Docker Container
- docker run -p hostport:containerport -v hostpath:'containerpath' -t -i bamos/openface /bin/bash
- Example: 
docker run -p 9000:9000 -p 8000:8000 -v /home/jeavio/Documents/Kaustubh/ML/Projects/Face-Recognition-with-Openface:'/bamos/kaustubh/Face-Recognition-with-Openface' -t -i bamos/openface /bin/bash

#### References
##### Install Docker
- [Docker Installation Guide](https://docs.docker.com/v17.12/install/)
