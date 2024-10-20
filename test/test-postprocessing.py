import unittest
import os
from postprocessing import postprocess_text

class TestPostprocessing(unittest.TestCase):
    
    def setUp(self):
        # Create test directories
        self.input_dir = "test_postprocess_input"
        self.output_dir = "test_postprocess_output"
        
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Write a sample translated file in the input directory
        with open(os.path.join(self.input_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("привет мир")  # Example translated text "hello world"

    def tearDown(self):
        # Clean up the test directories after the test is complete
        for dir_path in [self.input_dir, self.output_dir]:
            for file in os.listdir(dir_path):
                os.remove(os.path.join(dir_path, file))
            os.rmdir(dir_path)
    
    def test_postprocessing(self):
        # Run the postprocessing function
        postprocess_text(self.input_dir, self.output_dir)
        
        # Check if the output file exists and has been processed correctly
        output_file = os.path.join(self.output_dir, "test.txt")
        self.assertTrue(os.path.exists(output_file))
        
        # Read and check the content of the output file
        with open(output_file, 'r', encoding='utf-8') as f:
            processed_text = f.read()
            
        # Assuming the postprocessing adds capitalization
        self.assertEqual(processed_text, "Привет мир.")

if name == 'main':
    unittest.main()
