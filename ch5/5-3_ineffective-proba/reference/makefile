.SILENT:

SOURCES := $(wildcard *.c)
OBJECTS := $(patsubst %.c,%.o,$(SOURCES))
DEPENDS := $(patsubst %.c,%.d,$(SOURCES))

# ADD MORE WARNINGS!
WARNING := -w

# .PHONY means these rules get executed even if
# files of those names exist.
.PHONY: all clean

# The first rule is the default, ie. "make",
# "make all" and "make parking" mean the same
all: main

clean:
	$(RM) $(OBJECTS) $(DEPENDS) main *.txt

# Linking the executable from the object files
main: $(OBJECTS)
	$(CC) $(WARNING) $(CFLAGS) $^ -o $@

-include $(DEPENDS)

%.o: %.c makefile
	$(CC) $(WARNING) $(CFLAGS) -MMD -MP -c $< -o $@