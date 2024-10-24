ifeq ($(OS),Windows_NT)
	INPUT_RAW = %cd%\input_raw
	OUTPUT = %cd%\output
	/ := \\
	RM = del
else
	INPUT_RAW = `pwd`/input_raw
	OUTPUT = `pwd`/output
	/ := /
	RM = rm -fr
endif



# Variables for directory paths

DOCKER_IMAGE = translator

# Target to run the Docker container with the correct mounts
run:
	@echo "Running Docker container for translation..."
	docker run --rm -v $(INPUT_RAW):/app/input_raw \
	           -v $(OUTPUT):/app/output \
	           $(DOCKER_IMAGE)

build:
	docker build -t $(DOCKER_IMAGE)  .  --file Dockerfile

# Target to test the application
test:
	@echo "Running tests inside Docker container..."
	# docker run --rm $(DOCKER_IMAGE) pytest

# Optional: clean up the directory if needed
clean:
	@echo "Cleaning up output directory..."
	$(RM) $(OUTPUT)$(/)*

