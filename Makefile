CC = gcc
LEX = flex
YACC = bison
CFLAGS = -Wall -Wextra -g -O2
LDFLAGS = -lm

# Target executable
TARGET = brolang_parser

# Source files
LEXER_SOURCE = brolang_lexer.l
PARSER_SOURCE = brolang_parser.y
SUPPORTS = parser_utils.h

# Generated files
LEXER_GEN = lex.yy.c
PARSER_GEN_H = brolang_parser.tab.h
PARSER_GEN_C = brolang_parser.tab.c

# Object files
LEXER_OBJ = lex.yy.o
PARSER_OBJ = brolang_parser.tab.o

.PHONY: all clean test

all: $(TARGET)

$(TARGET): $(LEXER_OBJ) $(PARSER_OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(LEXER_OBJ) $(PARSER_OBJ) $(LDFLAGS)

$(PARSER_GEN_C) $(PARSER_GEN_H): $(PARSER_SOURCE) $(SUPPORTS)
	$(YACC) -d -o $(PARSER_GEN_C) $(PARSER_SOURCE)

$(LEXER_GEN): $(LEXER_SOURCE) $(PARSER_GEN_H)
	$(LEX) -o $(LEXER_GEN) $(LEXER_SOURCE)

$(LEXER_OBJ): $(LEXER_GEN)
	$(CC) $(CFLAGS) -c -o $(LEXER_OBJ) $(LEXER_GEN)

$(PARSER_OBJ): $(PARSER_GEN_C)
	$(CC) $(CFLAGS) -c -o $(PARSER_OBJ) $(PARSER_GEN_C)

test: $(TARGET)
	@echo "Testing with valid test cases:"
	@for testfile in testcases/valid/*.bro; do \
		echo "\n--- Testing: $$testfile ---"; \
		./$(TARGET) "$$testfile"; \
	done
	@echo "\n\nTesting with invalid test cases:"
	@for testfile in testcases/invalid/*.bro; do \
		echo "\n--- Testing (expected error): $$testfile ---"; \
		./$(TARGET) "$$testfile" || true; \
	done

clean:
	rm -f $(LEXER_GEN) $(LEXER_OBJ) $(PARSER_GEN_C) $(PARSER_GEN_H) $(PARSER_OBJ) $(TARGET) *.o

.PHONY: $(PARSER_GEN_H)
