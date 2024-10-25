import os
import sys
import pytest
import shutil
sys.path.append("src")
from preprocessing import preprocess_text

# Create a temporary directory for testing
@pytest.fixture
def temp_dirs(tmp_path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    input_dir.mkdir()
    output_dir.mkdir()
    return input_dir, output_dir

def create_sample_file(directory, filename, content):
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(content)

def test_valid_inputs(temp_dirs):
    input_dir, output_dir = temp_dirs
    
    # Create valid input files
    create_sample_file(input_dir, "valid1.txt", "This is a valid text file.")
    create_sample_file(input_dir, "valid2.txt", "This is another valid text file with numbers 12345 and symbols : ().")

    # Run the preprocessing
    preprocess_text(str(input_dir), str(output_dir))

    # Check that output files are created and their contents are equal to input files
    for file_name in ["valid1.txt", "valid2.txt"]:
        input_file_path = os.path.join(input_dir, file_name)
        output_file_path = os.path.join(output_dir, file_name)

        assert os.path.exists(output_file_path)
        
        # Compare contents of the input and output files
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            input_content = input_file.read().strip()
        
        with open(output_file_path, 'r', encoding='utf-8') as output_file:
            output_content = output_file.read().strip()

        assert input_content == output_content, f"Contents of {file_name} do not match."

def test_invalid_file_extension(temp_dirs, capsys):
    input_dir, output_dir = temp_dirs
    
    # Create an invalid input file
    create_sample_file(input_dir, "invalid1.csv", "This is an invalid file.")

    # Run the preprocessing
    preprocess_text(str(input_dir), str(output_dir))

    # Capture the output
    captured = capsys.readouterr()
    assert "There is a bad file in the data directory: invalid1.csv. File must be in txt extention" in captured.out

def test_cpp_validator(temp_dirs):
    input_dir, output_dir = temp_dirs
    
    # Run the preprocessing
    preprocess_text("test/hex", str(output_dir))

    # Check the contents of the output file
    with open(os.path.join(output_dir, "utf.txt"), 'r', encoding='utf-8') as f:
        content = f.read()

    # Assert that the output content does not contain the non-UTF-8 symbols
    expected_content = "Physics is like magic, but is real.\n"
    assert content == expected_content, f"Expected content: {expected_content}, but got: {content}"

# Cleanup after tests
def test_cleanup(temp_dirs):
    input_dir, output_dir = temp_dirs
    
    # Create valid input files
    create_sample_file(input_dir, "cleanup_file.txt", "This file will be cleaned up.")

    # Run the preprocessing
    preprocess_text(str(input_dir), str(output_dir))

    # Check if the output file exists
    assert os.path.exists(os.path.join(output_dir, "cleanup_file.txt"))

    # Clean up the directories
    shutil.rmtree(input_dir)
    shutil.rmtree(output_dir)

