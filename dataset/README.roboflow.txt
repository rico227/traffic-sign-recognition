
GTSDB - German Traffic Sign Detection Benchmark - v3 augmented-Roboflow-ACCURATE-model
==============================

This dataset was exported via roboflow.com on August 30, 2022 at 11:14 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 1311 images.
Signs are annotated in YOLO v7 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Randomly crop between 0 and 10 percent of the image
* Random rotation of between -10 and +10 degrees
* Random brigthness adjustment of between -15 and +15 percent
* Random exposure adjustment of between -15 and +15 percent
* Random Gaussian blur of between 0 and 0.75 pixels


