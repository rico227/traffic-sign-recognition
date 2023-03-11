SET yolopath=c:/repos/yolov7
docker rm yolov7 
docker run --name yolov7 --gpus=all -it -v %yolopath%:/workspace/yolov7 --shm-size=64g yolov7
