import os
import pytest
import sys
import shutil
sys.path.append('src')
from processing import translate_text

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

def test_translate_text(temp_dirs):
    input_dir, output_dir = temp_dirs

    # Create sample input files with English text
    create_sample_file(input_dir, "sample1.txt", "Hello.")
    create_sample_file(input_dir, "sample2.txt", "33 cows.")

    # Run the translation function
    translate_text(str(input_dir), str(output_dir))

    # Check that output files are created
    for file_name in ["sample1.txt", "sample2.txt"]:
        output_file_path = os.path.join(output_dir, file_name)
        assert os.path.exists(output_file_path)

        # Read the output content
        with open(output_file_path, 'r', encoding='utf-8') as out_f:
            translated_content = out_f.read().strip()

        if file_name == "sample1.txt":
            expected_translation = "Привет."  # Example expected translation
        elif file_name == "sample2.txt":
            expected_translation = "33 коровы."  # Example expected translation

        # Assert that the translated content matches the expected translation
        assert translated_content == expected_translation, f"Translation for {file_name} does not match."

# Cleanup after tests
def test_cleanup(temp_dirs):
    input_dir, output_dir = temp_dirs
    
    # Create valid input files
    create_sample_file(input_dir, "cleanup_file.txt", "This file will be cleaned up.")

    # Run the translation
    translate_text(str(input_dir), str(output_dir))

    # Check if the output file exists
    assert os.path.exists(os.path.join(output_dir, "cleanup_file.txt"))

    # Clean up the directories
    shutil.rmtree(input_dir)
    shutil.rmtree(output_dir)

