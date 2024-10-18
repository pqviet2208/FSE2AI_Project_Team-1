# import libraries
from transformers import MarianMTModel, MarianTokenizer

# Sequence to translate
src_text = [
    "Hello, how are you?"
]

# Pretrained model. Loading the model
model_name = "Helsinki-NLP/opus-mt-en-ru"
tokenizer = MarianTokenizer.from_pretrained(model_name)

model = MarianMTModel.from_pretrained(model_name)

# Run the model (Translate)
translated = model.generate(**tokenizer(src_text, return_tensors="pt", padding=True))
ru_tran = [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

# Print translated sequence
print(ru_tran)
