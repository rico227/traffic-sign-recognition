SET mypath=%~dp0
SET yolopath=c:/repos
docker rm yolov7 
docker run --name yolov7 --gpus=all -it -v %mypath:~0,-1%/GTSDB-1:/workspace/dataset/ -v %yolopath%/yolov7:/workspace/yolov7 --shm-size=64g yolov7