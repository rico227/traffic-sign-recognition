# Traffic Sign Recognition with machine learning

## Setup
### Create conda environment
- Download and install anaconda (https://conda.io/projects/conda/en/latest/user-guide/install/index.html)
- Open the anaconda powershell prompt and navigate to this repository
- To create a new conda environment with the packages needed run:
```
conda env create -f environment.yml
``` 
- To activate the conda environment run:
```
conda activate yolo
``` 
### Setup docker environment
- Download and install docker desktop (https://www.docker.com/products/docker-desktop/)
- To build a docker container the *Dockerfile* in root of this repository is used
- Build the docker container using a shell to run:
```
.\build_docker.bat
```
- Make sure the variable *'yolopath'* in the *start_docker.bat* is set to your local yolov7 directory path
- Start the docker container using a shell to run:
```
.\start_docker.bat
```

## Costum dataset
- Using images from the German Traffic Sign Recognition Benchmark (GTSRB) (Source: https://benchmark.ini.rub.de/gtsrb_news.html)
- Retrieve in yolov7-format labeled data of the GTSRB from Roboflow by running the *create_dataset.py*-script:
```
python create_dataset.py
```
- Note that you have to create a free Roboflow (https://roboflow.com/) account to get an API key 
- The retrieved key has to be set in the *create_dataset.py*

## AI enhanced dataset
- Using images generated by an AI to enhance the dataset
- For image generation the DALL-E (https://openai.com/blog/dall-e/) model is used
- Use the *Generate_Dataset.ipynb*-notebook for further information

## Training/Testing/Inference 
- To train the model run the YoloV7 (https://arxiv.org/abs/2207.02696) object detector model is used
- To use the YoloV7 functions start the docker container and navigate to the yolov7 directory in the container:
```
.\start_docker.bat
cd yolov7
```
- Training/Testing/Inference-results are put out in the 'runs'-directory


### Testing
- To test a model run in your docker container:
```
python test.py --data dataset/data.yaml --img 640 --batch 4 --conf 0.001 --iou 0.65 --device 0 --weights runs/train/yolov7-mixed/weights/best.pt --name test_mixed_dataset
```

### Training
- To train a model run in your docker container
```
python train.py --workers 8 --data dataset/data.yaml --cfg cfg/training/yolov7-tfr.yaml --img 640 640 --batch 4  --device 0 --weights 'yolov7_training.pt' --name train_mixed_dataset --hyp data/hyp.scratch.custom.yaml
```

### Inference
- To run inference on a video or an image run:
```
python detect.py --weights runs/train/yolov7-mixed/weights/best.pt --conf 0.5 --img-size 640 --source yourvideo.mp4
```
```
python detect.py --weights runs/train/yolov7-mixed/weights/best.pt --conf 0.5 --img-size 640 --source inference/images/your-image.jpg
```

## References
1. https://arxiv.org/abs/2207.02696#
2. https://github.com/WongKinYiu/yolov7
3. https://benchmark.ini.rub.de/gtsrb_news.html
4. https://docs.roboflow.com/
5. https://openai.com/blog/dall-e/