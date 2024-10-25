# Team-1_FSE

Topic: Application for Translation using Neural Network

Authors: QuocViet Pham, Svetlana Pavlova, Thanakrit Lerdmatayakul

---
# English to Russian Translation

## Project Overview

This project provides a pipeline for translating text from English to Russian using a pretrained model. It includes preprocessing, processing (translation), and postprocessing steps.

## How to Run

### Locally
- First, Clone the repository to your local machine
    ```bash
    github clone https://github.com/pqviet2208/FSE2AI_Project_Team-1.git
    ```
    ```bash
    cd FSE2AI_Project_Team-1
    ```

1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the pipeline:
    ```bash
    make run
    ```

### Using Docker

- First, Clone the repository to your local machine
    ```bash
    github clone https://github.com/pqviet2208/FSE2AI_Project_Team-1.git
    ```
    ```bash
    cd FSE2AI_Project_Team-1
    ```

1. Build the Docker image:
    ```bash
    make build
    ```

2. To run the app:
    ```bash
    make run
    ```
    Note: wait for some time for the model to run

## How to Test

Run the following command to execute all tests:
```bash
make test
```

## Source Directory is separated into 4 files:
> [preprocessing.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/preprocessing.py)`
  Takes raw input data and processes it into a format suitable for translation.
- Check if the files in the data folder has .txt extention
- verify the utf-8 format to get rid of any broken symbols and remove them

> [processing.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/processing.py)`
- Script for the processing (translation) step. Translates the preprocessed data using the **MarianMTModel**
- https://huggingface.co/docs/transformers/en/model_doc/marian

> [postprocessing.py](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/postprocessing.py)`
- Capitalize the first letter in the text file and merge input text with translated text into one file




