# Install dependencies
prereqs:
	pip install -r requirements.txt

# Build step (if needed)
build:
	echo "Nothing to build for now"

# Run preprocessing step
preprocess:
	python src/preprocessing.py --input input_raw --output input

# Run processing step (translation)
process:
	python src/processing.py --input input --output output_raw

# Run postprocessing step
postprocess:
	python src/postprocessing.py --input output_raw --output output

# Run full pipeline (preprocess -> process -> postprocess)
run:
	preprocess process postprocess

# Run all tests
test:
	python test/test_preprocessing.py
	python test/test_processing.py
	python test/test_postprocessing.py
