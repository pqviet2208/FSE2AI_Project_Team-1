from transformers import MarianMTModel, MarianTokenizer
import os
import argparse

def translate_text(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    model_name = "Helsinki-NLP/opus-mt-en-ru"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    
    for file_name in os.listdir(input_dir):
        with open(os.path.join(input_dir, file_name), 'r', encoding='utf-8') as f:
            src_text = f.read().strip()
            translated = model.generate(**tokenizer([src_text], return_tensors="pt", padding=True))
            ru_tran = tokenizer.decode(translated[0], skip_special_tokens=True)
            
            with open(os.path.join(output_dir, file_name), 'w', encoding='utf-8') as out_f:
                out_f.write(ru_tran)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Translate text from English to Russian")
    parser.add_argument('--input', required=True, help="Input directory with preprocessed text files")
    parser.add_argument('--output', required=True, help="Output directory for translated text files")
    args = parser.parse_args()
    
    translate_text(args.input, args.output)
