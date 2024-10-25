import os
import argparse

def postprocess_text(raw_dir, input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    delim = '-='*20

    for file_name in os.listdir(input_dir):
        with open(os.path.join(input_dir, file_name), 'r', encoding='utf-8') as f:
            with open(os.path.join(raw_dir, file_name), 'r') as fraw:
                init_text = fraw.read() 
            text = f.read()
            # Add custom postprocessing like formatting
            formatted_text = text.capitalize()  # Example of formatting
            with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as out_f:
                out_f.write(init_text + '\n' + delim + '\n' + formatted_text + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Postprocess translated text")
    parser.add_argument('--raw', required=True, help="Raw directory with initial text files")
    parser.add_argument('--input', required=True, help="Input directory with translated text files")
    parser.add_argument('--output', required=True, help="Output directory for postprocessed text files")
    args = parser.parse_args()
    
    postprocess_text(args.raw, args.input, args.output)
