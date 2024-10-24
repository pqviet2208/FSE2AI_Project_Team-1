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

 0. First, Clone the repository to your local machine
    ```bash
    github clone https://github.com/pqviet2208/FSE2AI_Project_Team-1.git
    ```
    ```bash
    cd FSE2AI_Project_Team-1
    ```

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
```

## Source Directory is separated into 4 files:
> [preprocessing.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/preprocessing.py)`
-  Script for the preprocessing step. Takes raw input data and processes it into a format suitable for translation.

> [processing.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/processing.py)`
- Script for the processing (translation) step. Translates the preprocessed data using the MarianMTModel

> [postprocessing.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/postprocessing.py)`
- Postprocesses translated text files by applying custom formatting or other modifications

> [translator.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/translator.py)`




