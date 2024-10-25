
NAME = validate
CFLAGS = $(shell pkg-config --cflags glib-2.0)
LFLAGS = $(shell pkg-config --libs glib-2.0)

all: $(NAME)

validate: $(NAME).cpp
	g++ $(CFLAGS) $(NAME).cpp -o $(NAME) $(LFLAGS)

clean: $(NAME).cpp
	rm -f $(NAME)
