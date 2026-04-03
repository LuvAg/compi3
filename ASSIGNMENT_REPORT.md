# CS327 Compilers Assignment 3 Report
## LALR(1) Parser Construction and Conflict Resolution

**Course:** CS327 Compilers  
**Instructor:** Shouvick Mondal  
**Semester:** January-May 2026  

**Group Members:**
- Rachit Mehta (23110261)
- Luv Agarwal (23110189)
- Prateek Takshak (23110256)


---

## Objective

This report demonstrates:
1. Construction of the LALR(1) automaton.
2. Identification of shift/reduce and reduce/reduce conflicts.
3. Grammar-level conflict resolution.
4. Before/after conflict-resolution parsing behavior.
5. Reverse derivation tree output after successful parsing.
6. Parsing table output in matrix format.
7. Informative error diagnostics.

## Important Notes

- The parsing table follows the matrix format used in lecture slides.
- Conflicts in the automaton are identified and explicitly explained.
- Error diagnostics are implemented as a core deliverable.

---

## Executive Summary

This assignment implements a complete LALR(1) parser for the **Brolang** programming language with:
- **Part 1:** Full LALR(1) automaton construction (101 states)
- **Part 2:** Conflict identification and resolution (0 conflicts)
- **Part 3:** Reverse derivation tree display (post-order traversal)
- **Part 4:** Detailed LALR(1) parsing table in matrix format
- **Part 5:** Comprehensive error diagnostics system
- **Part 6:** Additional implementation details and analysis

---

## Part 1: LALR(1) Automaton Construction

### Methodology
The LALR(1) automaton is constructed using the Bison/Yacc parser generator with the following process:

1. **Grammar Definition:** 45 production rules covering all language constructs
2. **Item Set Construction:** Closure and goto operations on LR(0) items
3. **LALR(1) Merging:** Merging of LR(0) states based on LALR(1) lookahead sets
4. **Conflict Detection:** Automatic detection of shift/reduce and reduce/reduce conflicts

### Grammar Rules (Reference)
```
R0:  program → HIBRO stmts BYEBRO
R1:  stmts → ε (empty)
R2:  stmts → stmts stmt
R3-R5:  stmt → declarations/constants
R6-R7:  stmt → assignments/print
R8-R10: stmt → assertions/break/continue
R11-R15: stmt → control flow (if/elif/else/while)
R16-R19: type_name → NUM | STR | BOOL | NALLA
R20-R24: assign_op → = | += | -= | *= | /=
R25:    block → LBRACE stmts RBRACE
R26-R27: expr_list → expressions
R28-R40: expr → literals, identifiers, binary/unary ops, parentheses
R41-R45: literal → NUMBER | STRING | SAHI | GALAT | NIL
```

### Key Parser States
```
State 0 (Initial):
  S' → • program
  program → • HIBRO stmts BYEBRO
  ACTION: shift HIBRO → State 1

State 1 (After HIBRO):
  program → HIBRO • stmts BYEBRO
  stmts → • ε
  stmts → • stmts stmt
  ACTION: reduce (empty) or shift stmt

State 5 (Expression Parsing):
  expr → expr • PLUS expr    (shift arithmetic)
  expr → expr • MINUS expr   (left-associative)
  expr → expr • MUL expr     (higher precedence)
  expr → expr • DIV expr
  ACTION: shift operators (governed by precedence)

...101 total states with explicit action/goto entries
are present in later section of All_state_details.md


Conflict C1: Dangling else shift/reduce conflict
State observed: 18
Type: Shift/Reduce
Productions involved:
stmt -> AGARBRO ( expr ) block
stmt -> AGARBRO ( expr ) block WARNABRO block
Explanation: The parser can either reduce a completed if statement or shift WARNABRO to continue into an else branch.
Resolution applied: Reworked conditional grammar into explicit if/elif/else forms to remove ambiguity.
Final status: Resolved (no remaining conflict for this pattern).


Conflict C2: Expression operator boundary shift/reduce risk
States observed: Expression parsing states where operators compete
Type: Shift/Reduce risk (precedence and associativity related)
Productions involved:
expr -> expr PLUS expr
expr -> expr MINUS expr
expr -> expr MUL expr
expr -> expr DIV expr


- **Explicit States (C2):** 30, 45, 58, 59, 60, 61, 66, 67, 68, 69, 70, 71, 72, 73, 74, 81

State interpretation for C2:
- **Operator lookahead states:** 30, 45, 58, 59, 60, 61, 66, 81 (parser sees `expr • op expr` and decides continuation at operator boundaries)
- **Reduce-vs-continue states after RHS parse:** 67, 68, 69, 70, 71, 72, 73, 74 (completed expression plus possible next operator)

Explanation: Without precedence rules, parser actions are ambiguous when deciding between reducing the current expression or shifting the next operator.
Resolution applied: Added precedence and associativity declarations for arithmetic operators.
Final status: Resolved.


Conflict C3: Reduce/reduce conflict check
States observed: None 
Type: Reduce/Reduce
Productions involved: None (no overlapping completed items with same lookahead)
Explanation: No state produced simultaneous competing reductions after grammar finalization.
Resolution applied: Not required.
Final status: No reduce/reduce conflicts present.
---

## Part 2: Conflict Identification & Resolution

### Original Grammar Issues

#### Conflict #1: Shift/Reduce on Dangling Else (RESOLVED ✓)
- **Type:** Shift/Reduce conflict
- **State:** 18 (nested if without else)
- **Lookahead:** WARNABRO (else)
- **Issue:** In `if (...) { if (...) {} else {} }`, parser couldn't determine clause binding

**Original Problem:**
```
stmt → AGARBRO ( expr ) block            {Rule 1}
stmt → AGARBRO ( expr ) block WARNABRO block  {Rule 2}
```
When seeing WARNABRO after first block:
- SHIFT? Continue to see if there's else
- REDUCE? Finish current if

**Resolution:** Explicit grammar rules for all if-elif-else combinations
```
stmt → AGARBRO ( expr ) block                          {if only}
stmt → AGARBRO ( expr ) block NAITOBRO ( expr ) block  {if-elif}
stmt → AGARBRO ( expr ) block WARNABRO block           {if-else}
stmt → AGARBRO ( expr ) block NAITOBRO ( expr ) block WARNABRO block  {if-elif-else}
```
**Result:** Grammar is now **unambiguous**. Else always binds correctly.

#### Conflict #2: Operator Precedence (RESOLVED ✓)
- **Type:** Implicit S/R conflicts
- **Operators:** +, -, *, / (arithmetic); <, >, <=, >=, ==, != (comparison)

**Original Issue:** `a + b * c` could parse as `(a+b)*c` or `a+(b*c)`

**Resolution:** Operator precedence declarations
```yacc
%left COMMA              (lowest precedence)
%left LT GT LE GE EQ NEQ (comparison)
%left PLUS MINUS         (addition/subtraction)
%left MUL DIV            (multiplication/division - highest)
```
**Result:** Correct operator precedence and **left-associativity** for all binary operators.

#### Conflict #3: Reduce/Reduce Conflicts (NONE ✓)
Each statement type has **unique starting terminal:**
- `BRO` → variable declaration
- `PAKKA` → constant declaration
- `IDENTIFIER` → assignment
- `BOLBRO` → print
- `BROASSERT` → assertion
- `BASKARBRO` → break
- `AGLADEHBRO` → continue
- `AGARBRO` → if statement
- `JABTAKBRO` → while loop

**Result:** No ambiguity possible. **Zero reduce/reduce conflicts.**

### Before & After Examples

**Example 1: Nested If-Else**
```brolang
hibro
agarbro (sahi) {
  agarbro (sahi) {
    bolbro 1;
  }
  warnabro {
    bolbro 2;
  }
}
byebro
```

BEFORE (with original grammar):
- Shift/Reduce conflict in state 18
- Parser uses default resolution (shift)
- Behavior is implicit, not guaranteed by grammar

AFTER (with conflict-free grammar):
-  No conflicts
- Grammar explicitly handles all if-elif-else combinations
- Parser behavior is deterministic and guaranteed

**Example 2: Arithmetic Expression Evaluation**
```brolang
bro num x = 2 + 3 * 4 - 1;
// Expected: ((2 + (3 * 4)) - 1) = 13
```

Parsing Process:
1. Shift 2 (expr)
2. See +, may shift or reduce
3. Lookahead * has higher precedence
4. Shift and continue: 3 * 4 = 12
5. Reduce: 2 + 12 = 14
6. See -, shift and reduce: 14 - 1 = 13 ✓

---

## Part 3: Reverse Derivation Tree

In terminal type: make part3
Output in PART3_REVERSE_DERIVATION_TREES.txt
Run make part3-pretty
Output in  PART3_DERIVATION_TREE_PRETTY.md 
has detailed view
Run make part3-graphs
Also has in png format
## Part 4: LALR(1) Parsing Table

The complete parsing table is generated by Bison during compilation and includes:

### Action Table (abbreviated sample):
```
State │  HIBRO   │  BYEBRO  │ BRO │ PAKKA │ NUM │ ... │ Other
──────┼──────────┼──────────┼─────┼───────┼─────┼─────┼─────
  0   │ shift 1  │          │     │       │     │     │ err
  1   │          │ reduce   │ s3  │  s2   │     │     │ reduce
  2   │          │          │ s7  │  s8   │     │     │
  3   │          │          │ s7  │  s8   │     │     │
  ... │          │          │     │       │     │     │
```

### Notation:
- `s N` = Shift token, go to state N
- `r N` = Reduce using rule N
- `acc` = Accept (program complete)
- `err` = Syntax error
- (blank) = No valid action

### Goto Table (Non-terminals):
```
State │ program │ stmts │ stmt │ type_name │ block │ expr │ expr_list
──────┼─────────┼───────┼──────┼───────────┼───────┼──────┼──────────
  0   │    1    │   2   │  3   │     -     │   -   │  -   │    -
  1   │    -    │   -   │  4   │     -     │   -   │  -   │    -
  2   │    -    │   -   │  -   │     5     │   -   │  -   │    -
  ... │         │       │      │           │       │      │
```

The complete table with all 101 states is embedded in 
PART4_ACTION_GOTO_TABLE.txt
This can be genereted by running make part4

## Part 5: Error Diagnostics System

The parser provides comprehensive error detection and reporting:

### Error Categories

**1. Lexical Errors**
- Unknown tokens (non-matching characters)
- Invalid number/string literals
- Malformed operators

**2. Syntax Errors (Shift/Reduce Parser)**
- Unexpected tokens
- Missing required tokens (semicolons, parentheses, braces)
- Invalid statement structure
- Missing block bodies

**3. Structural Errors**
- Missing `hibro` start marker
- Missing `byebro` end marker
- Unmatched parentheses/braces
- Unclosed blocks

**4. Declaration Errors**
- Missing type in variable declaration
- Invalid type name (integer, float, etc.)
- Missing variable name
- Missing initializer for constants

**5. Expression Errors**
- Empty expressions
- Invalid operators in context
- Unmatched parentheses

### Example Error Reports


**Missing Semicolon:**
After running,
./brolang_parser testcases/invalid/test_missing_semicolon.bro
```
Input:
  hibro
  bro num x = 10
  bolbro x;
  byebro

Output:
  Parsing failed with 1 error(s)
  Syntax Error at line 2: expecting ; after variable declaration
```

**Missing Closing Brace:**
```
After running,
./brolang_parser testcases/invalid/test_missing_brace.bro
Input:
  hibro
  agarbro (sahi) {
    bolbro 42;
  byebro

Output:
  Parsing failed with 1 error(s)
  Syntax Error at line 4: expecting } to close block
```

**Invalid Type:**
After running,
./brolang_parser testcases/invalid/test_invalid_type.bro
```
Input:
  hibro
  bro integer x = 42;
  byebro

Output:
   Parsing failed with 1 error(s)
  Syntax Error at line 2: unexpected token 'integer'
``


---

## Part 6: Additional Information

### Implementation Architecture

**Lexer (brolang_lexer.l)**
- Flex-based tokenizer
- ~60 patterns for Brolang tokens
- Multi-line comment support
- Line number tracking
- String literal handling (both quotes)

**Parser (brolang_parser.y)**
- Bison/Yacc LALR(1) parser
- 45 production rules
- Clean semantic actions
- Parse tree construction
- Error handling

**Utilities (parser_utils.h)**
- Parse tree node structures
- Reverse traversal (post-order)
- Memory management
- Parsing table display
- Conflict analysis
- Error diagnostic output

### Performance Characteristics
- **Lexer:** O(n) single-pass tokenization
- **Parser:** O(n) shift-reduce parsing
- **Memory:** O(d) for parser stack (d = parse depth)
- **Trees:** O(n) space for parse tree (n = tokens)

### Build System
```makefile
LEXER:   flex → brolang_lexer.l → lex.yy.c
PARSER:  bison → brolang_parser.y → brolang_parser.tab.c/h
COMPILE: gcc → link lex.yy.o + brolang_parser.tab.o → brolang_parser
```

### Testing
Created comprehensive test suite:
```
testcases/valid/
  - test1_basic.bro          (simple variable + print)
  - test2_if_else.bro        (if-else statements)
  - test3_loop.bro           (while loop)
  - test4_arithmetic.bro     (precedence test)
  - test5_nested_if.bro      (nested if-else)
  - test6_constants.bro      (const declarations)

testcases/invalid/
  - test_missing_semicolon.bro
  - test_missing_brace.bro
  - test_invalid_type.bro
```

### Key Features
 **Conflict-Free Grammar** - No shift/reduce or reduce/reduce conflicts
 **Correct Precedence** - Operator precedence and associativity properly defined
 **Robust Parsing** - Handles complex nested structures
 **Informative Errors** - Detailed diagnostics with line numbers
 **Complete Language** - Supports all Brolang constructs
 **Memory Efficient** - O(input size) space complexity
 **Production Quality** - Error recovery and proper resource cleanup

---

## Conclusion

The LALR(1) parser for Brolang is **complete, conflict-free, and fully functional**. It successfully:
1. Constructs an LALR(1) automaton with 101 states
2. Identifies and resolves conflicts through grammar modifications
3. Displays parse trees in reverse order via post-order traversal
4. Outputs comprehensive LALR(1) parsing tables
5. Provides detailed error diagnostics and recovery suggestions
6. Implements all required features with production-quality code

