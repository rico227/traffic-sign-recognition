#!/bin/sh
DATASET_LOCATION=dataset
python train.py --batch 2 --epochs 10 --cfg cfg/training/yolov7.yaml --weights yolov7_training.pt --data $DATASET_LOCATION/data.yaml --device 0