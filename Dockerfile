#!/usr/bin/env -S docker build -t translator  .  --file


# Use clean UBUNTU 24.04  as the base image
FROM  ubuntu:24.04

# Set environment variables to avoid issues with buffer or input output handling
ENV PYTHONUNBUFFERED=1
ENV HOME=/root

RUN apt update && apt install -y bash  make git curl ca-certificates build-essential gcc vim python3 python3-pip python3-venv pkg-config libglib2.0-dev

RUN python3 -m venv /python
RUN echo "source /python/bin/activate" > /root/.profile && echo "source /python/bin/activate" > /root/.bashrc

RUN bash -l -c "python3 -m pip install  torch==2.5.0"
# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the project files into the container
COPY . .
COPY Makefile.inside_docker Makefile


# Run the pipeline using the main Makefile
RUN bash -l -c "make -f Makefile.docker prereqs"
RUN bash -l -c "make -f Makefile.docker build"
RUN bash -l -c "make -f Makefile.docker clean"
#RUN bash -l -c "make -f Makefile.docker test"

CMD bash -l -c "make run"

