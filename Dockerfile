FROM  nvcr.io/nvidia/pytorch:21.08-py3

# apt install required packages
RUN apt update && apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
RUN pip install seaborn thop

# copy scripts
COPY *.sh /workspace/scripts/