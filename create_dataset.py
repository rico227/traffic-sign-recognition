import os
import re
from roboflow import Roboflow

# constants
DATASET_NAME = "GTSDB---German-Traffic-Sign-Detection-Benchmark"
API_KEY = "Ab8pO3HNA4EBf2YOKkJc"
WORKSPACE_NAME = "mohamed-traore-2ekkp"
PROJECT_VERSION = 3
DATASET_FORMAT = "yolov7"
NEW_DATASET_NAME = "dataset"

# change working directory
os.chdir("../yolov7/")

# check if dataset exists
if os.path.exists(NEW_DATASET_NAME):
    # ask user if they want to delete the dataset
    delete = input("Dataset already exists. Do you want to delete it? (y/n): ")
    if delete == "y":
        # check operating system windows
        if os.name == "nt":
            # delete dataset
            os.system("rmdir /s /q " + NEW_DATASET_NAME)
        # check operating system linux    
        elif os.name == "posix":
            # delete dataset
            os.system("rm -rf " + NEW_DATASET_NAME)
    else:
        # exit
        exit()

# get dataset
rf = Roboflow(api_key=API_KEY)
project = rf.workspace(WORKSPACE_NAME).project(DATASET_NAME.lower())
dataset = project.version(PROJECT_VERSION).download(DATASET_FORMAT)

# rename dataset
os.rename(f"{dataset.location}", NEW_DATASET_NAME)

# rename string in yaml file
with open("dataset/data.yaml", "r") as file:
    filedata = file.read()
    old_dataset_name = f"{DATASET_NAME}-{PROJECT_VERSION}"
    filedata = filedata.replace(old_dataset_name, NEW_DATASET_NAME)
    
with open("dataset/data.yaml", "w") as writefile:
    writefile.write(filedata)        

