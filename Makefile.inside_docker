# Docker Entry Makefile (Makefile.docker)

# Run preprocessing step
preprocess:
	python3 src/preprocessing.py --input input_raw --output input

# Run processing (translation) step
process:
	python3 src/processing.py --input input --output output_raw

# Run postprocessing step
postprocess:
	python3 src/postprocessing.py --input output_raw --output output

# Run full pipeline (preprocess -> process -> postprocess)
run: preprocess process postprocess
