# Team-1_FSE

Topic: Application for Translation using Neural Network

Authors: QuocViet Pham, Svetlana Pavlova, Thanakrit Lerdmatayakul

## Table of Contents 

 - [Project Overview](#Project-Overview)
 - [Prerequisites](#Prerequisites)
 - [How to run](#How-to-Run)
 - [How to test](#How-to-Test) 
 - [Source Files](#Source-Directory-is-separated-into-3-files)

---
# English to Russian Translation

## Project Overview

This project provides a pipeline for translating text from English to Russian using a pretrained model. It includes preprocessing, processing (translation), and postprocessing steps.

## Prerequisites
- Docker is based on fresh ubuntu 24.04 
- Requires ~10GB of free disk space for image building, minimum 4G free RAM for smooth work. Internet connection is requered to run the app.
<!-- - At least **python 3.12.0** -->


- **Note:** <br />
 You will have a [**data directory**](https://github.com/pqviet2208/FSE2AI_Project_Team-1/tree/main/data) for inputting text. 
We have put for you some default data to translate, <br /> 
you can remove all files from data directory and put in `.txt` files .
 <br /> (Note that only `.txt` file will work)


## How to Run

### Locally
- First, Clone the repository to your local machine
    ```bash
    git clone https://github.com/pqviet2208/FSE2AI_Project_Team-1.git
    ```
    ```bash
    cd FSE2AI_Project_Team-1
    ```

1. Install the required dependencies:
    ```bash
    python3 -m pip install -r requirements.txt
    ```
    or
   ```bash
    python -m pip install -r requirements.txt
   ```
    or
   ```bash
    pip install -r requirements.txt
    ```

3. Compile the C++ code:
    ```bash
    (cd src/cpp_utils && make )
    ```
    
4. Run all tests:
    ```bash
    python3 -m pytest test/test_*.py
    ```
    or
   ```bash
    python -m pytest test/test_*.py
   ```
   or
   ```bash
    pytest test/test_*.py
    ```
    
3. Run translation pipeline:
    ```bash
    make run -f Makefile.inside_docker
    ```
4. Clean output directory:
   ```bash
   make clean
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

3. To clean output directory:
   ```bash
   make clean
   ```

## How to Test

Run the following command to execute all tests:
```bash
make test
```

## Source Directory is separated into 3 files:
> [**preprocessing.py**](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/preprocessing.py)`
- Check if the files in the data folder has .txt extention
- verify the utf-8 format to get rid of any broken symbols and remove them

> [**processing.py**](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/processing.py)`
- Script for the processing (translation) step. Translates the preprocessed data using the **MarianMTModel**
- https://huggingface.co/docs/transformers/en/model_doc/marian

> [**postprocessing.py**](https://github.com/pqviet2208/FSE2AI_Project_Team-1/blob/main/src/postprocessing.py)`
- Capitalize the first letter in the text file and merge input text with translated text into one file

## Example:
- **Input data**: 
 <br /> *"Once there was a kingdom with magical forest. In the forest there was a little frog."*

- **Output data**: 
 <br /> *"Once there was a kingdom with magical forest. In the forest there was a little frog. 
 <br /> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
 <br /> Когда-то было королевство с волшебным лесом, в лесу была маленькая лягушка
"*







