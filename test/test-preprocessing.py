import unittest
import os
from preprocessing import preprocess_text

class TestPreprocessing(unittest.TestCase):
    def test_preprocess(self):
        input_dir = "test_input"
        output_dir = "test_output"
        os.makedirs(input_dir, exist_ok=True)
        with open(os.path.join(input_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("Hello, WORLD!")
        
        preprocess_text(input_dir, output_dir)
        
        with open(os.path.join(output_dir, "test.txt"), 'r', encoding='utf-8') as f:
            processed_text = f.read()
            self.assertEqual(processed_text, "hello, world!")

if name == 'main':
    unittest.main()
