FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04



RUN apt-get update && apt-get install -y --no-install-recommends build-essential git vim curl python3 python3-dev python3-setuptools \
    python3-pip libglib2.0-0 libsm6 libfontconfig1 libxrender1 libxext6 ca-certificates wget bzip2

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install pandas bs4

WORKDIR /home

COPY . /home




