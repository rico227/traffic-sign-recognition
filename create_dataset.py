import os
from roboflow import Roboflow

# change working directory
os.chdir("../yolov7/")
# get dataset
rf = Roboflow(api_key="Ab8pO3HNA4EBf2YOKkJc")
project = rf.workspace("mohamed-traore-2ekkp").project("gtsdb---german-traffic-sign-detection-benchmark")
dataset = project.version(3).download("yolov7")
# rename dataset
os.rename(f"{dataset.location}", "dataset")
