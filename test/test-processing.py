import unittest
import os
from processing import translate_text

class TestProcessing(unittest.TestCase):
    def test_translate(self):
        input_dir = "test_input"
        output_dir = "test_output"
        os.makedirs(input_dir, exist_ok=True)
        with open(os.path.join(input_dir, "test.txt"), 'w', encoding='utf-8') as f:
            f.write("Hello, how are you?")
        
        translate_text(input_dir, output_dir)
        
        with open(os.path.join(output_dir, "test.txt"), 'r', encoding='utf-8') as f:
            translated_text = f.read()
            self.assertTrue("Привет" in translated_text)

if name == 'main':
    unittest.main()
