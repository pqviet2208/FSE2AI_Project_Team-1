# Team-1_FSE

Topic: Application for Translation using Neural Network
Authors: QuocViet Pham, Svetlana Pavlova, Thanakrit Lerdmatayakul

---
# English to Russian Translation

## Project Overview

This project provides a pipeline for translating text from English to Russian using a pretrained model. It includes preprocessing, processing (translation), and postprocessing steps.

## How to Run

### Locally

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the pipeline:
    ```bash
    make run
    ```

### Using Docker

1. Build the Docker image:
    ```bash
    docker build -t translation_pipeline .
    ```

2. Run the Docker container:
    ```bash
    docker run translation_pipeline
    ```

## How to Test

Run the following command to execute all tests:
```bash
make test

