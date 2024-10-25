import os
import argparse

def preprocess_text(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for file_name in os.listdir(input_dir):
        with open(os.path.join(input_dir, file_name), 'r', encoding='utf-8') as f:
            text = f.read().strip().lower()
            clean_text = ' '.join(text.split())
            with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as out_f:
                out_f.write(clean_text)

def preprocess_text(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for file_name in os.listdir(input_dir):
        if not file_name.endswith(".txt"):
            print("Bad file")
            continue
        fn = os.path.join(input_dir, file_name)
        out_fn = os.path.join(output_dir, file_name)
        os.system(f"src/cpp_utils/validate '{fn}' > {out_fn}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess English text")
    parser.add_argument('--input', required=True, help="Input directory with raw text files")
    parser.add_argument('--output', required=True, help="Output directory for preprocessed files")
    args = parser.parse_args()
    
    preprocess_text(args.input, args.output)

