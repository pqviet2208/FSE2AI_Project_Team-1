import os
import sys
import pytest
import shutil
sys.path.append('src')
from postprocessing import postprocess_text

# Create a temporary directory for testing
@pytest.fixture
def temp_dirs(tmp_path):
    raw_dir = tmp_path / "raw"
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"
    raw_dir.mkdir()
    input_dir.mkdir()
    output_dir.mkdir()
    return raw_dir, input_dir, output_dir

def create_sample_file(directory, filename, content):
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as f:
        f.write(content)

def test_postprocess_text_valid(temp_dirs):
    raw_dir, input_dir, output_dir = temp_dirs

    # Create sample raw and input files
    create_sample_file(raw_dir, "sample1.txt", "This is the original text.")
    create_sample_file(input_dir, "sample1.txt", "это перевод.")

    # Run the postprocessing function
    postprocess_text(str(raw_dir), str(input_dir), str(output_dir))

    # Check that output files are created
    output_file_path = os.path.join(output_dir, "sample1.txt")
    assert os.path.exists(output_file_path)

    # Read the output content
    with open(output_file_path, 'r', encoding='utf-8') as out_f:
        output_content = out_f.read()

    # Prepare expected content
    delim = '-=' * 20
    expected_content = "This is the original text.\n" + delim + "\nЭто перевод.\n"

    # Assert that the output content matches the expected content
    assert output_content == expected_content, f"Output content does not match for sample1.txt."


# Cleanup after tests
def test_cleanup(temp_dirs):
    raw_dir, input_dir, output_dir = temp_dirs
    
    # Create valid raw and input files
    create_sample_file(raw_dir, "cleanup_file.txt", "This is the original cleanup text.")
    create_sample_file(input_dir, "cleanup_file.txt", "this is the translated cleanup text.")

    # Run the postprocessing
    postprocess_text(str(raw_dir), str(input_dir), str(output_dir))

    # Check if the output file exists
    assert os.path.exists(os.path.join(output_dir, "cleanup_file.txt"))

    # Clean up the directories
    shutil.rmtree(raw_dir)
    shutil.rmtree(input_dir)
    shutil.rmtree(output_dir)


