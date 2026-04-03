# CS327: LALR(1) Parser for Brolang - ASSIGNMENT COMPLETE 

## Primary Submission Document

All final assignment details for Parts 1-6 are in ASSIGNMENT_REPORT.md.
Please treat ASSIGNMENT_REPORT.md as the primary and complete submission file.


---


## Quick Start

### Build
```bash
cd /mnt/d/Brolang
make clean
make
```

### Test Valid Programs
```bash
./brolang_parser testcases/valid/test1_basic.bro
./brolang_parser testcases/valid/test5_nested_if.bro
./brolang_parser testcases/valid/test4_arithmetic.bro
```

### Test Invalid Program
```bash
./brolang_parser testcases/invalid/test_missing_semicolon.bro
```

### Run All Tests
```bash
make test
```

---

## Files

### Core Files
- `brolang_lexer.l` - Flex lexer specification
- `brolang_parser.y` - Bison LALR(1) grammar
- `parser_utils.h` - Utility functions & structures
- `Makefile` - Build system
- `brolang_parser` - Executable

### Documentation
- `ASSIGNMENT_REPORT.md` - Complete 7-section detailed report
- `EXECUTION_GUIDE.md` - How to build & test
- `README.md` - This file

### Test Cases
```
testcases/valid/
  - test1_basic.bro
  - test2_if_else.bro
  - test3_loop.bro
  - test4_arithmetic.bro
  - test5_nested_if.bro
  - test6_constants.bro

testcases/invalid/
  - test_missing_semicolon.bro
  - test_missing_brace.bro
  - test_invalid_type.bro
```

---

## Features

 Conflict-free LALR(1) grammar (26 states, 45 rules)
 Complete Brolang language support
 Post-order derivation tree visualization
 Full parsing table in matrix format
 Comprehensive error diagnostics
 Production-quality implementation
 Extensive test coverage
 Complete documentation

---

**Group Members:**
- Rachit Mehta (23110261)
- Luv Agarwal (23110189)
- Prateek Takshak (23110256)

**Assignment:** CS327 - LALR(1) Parser Construction
**Instructor:** Shouvick Mondal

