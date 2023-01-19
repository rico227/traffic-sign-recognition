#!/bin/sh
python train.py --workers 8 --device 0 --batch-size 4 --epochs 500 --data dataset/data.yaml --img 640 640 --cfg cfg/training/yolov7-tfr.yaml --weights 'yolov7_training.pt' --name yolov7-ai --hyp data/hyp.scratch.custom.yaml