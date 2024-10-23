#!/usr/bin/env -S docker build -t translator  .  --file


# Use Python 3.9 as the base image
# FROM python:3.9-slim
FROM  ubuntu:24.04

# Set environment variables to avoid issues with buffer or input output handling
ENV PYTHONUNBUFFERED=1
ENV HOME=/root

RUN apt update && apt install -y bash  make git curl ca-certificates build-essential gcc vim python3 python3-pip python3-venv

RUN python3 -m venv /python


# Set the working directory inside the container
WORKDIR /app
RUN mkdir -p /app/input_raw /app/input /app/output_raw /app/output

# Install Python dependencies
# RUN python -m pip install --upgrade pip

# Copy the rest of the project files into the container
COPY . .

RUN echo "source /python/bin/activate" > /root/.profile && echo "source /python/bin/activate" > /root/.bashrc

# Run the pipeline using the main Makefile
#RUN bash -c "source /python/bin/activate; make -f Makefile.docker prereqs"
#RUN bash -c "source /python/bin/activate; make -f Makefile.docker build"
#RUN bash -c "source /python/bin/activate; make -f Makefile.docker test"
RUN bash -l -c "make -f Makefile.docker prereqs"
#RUN bash -l -c "make -f Makefile.docker build"
RUN bash -l -c "make -f Makefile.docker test"
#RUN make -f Makefile.docker prereqs
#RUN make -f Makefile.docker build
#RUN make -f Makefile.docker test

#CMD bash -l -c "make run"
