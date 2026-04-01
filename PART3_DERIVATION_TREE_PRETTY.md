# Part 3 - Reverse Derivation Trees (Improved Representation)

Generated on: 2026-04-01 17:36:04

Graph images: PNG files are available in part3_graphs/.

## Testcase: testcases/valid/test1_basic.bro

### Tree View (Post-Order)

```text
      └─ TYPE [num]
      └─ ID [x]
      └─ NUM [42]
    └─ DECLARATION
      └─ ID [x]
    └─ PRINT
  └─ STATEMENT
  └─ STATEMENT
└─ PROGRAM
```

### Graph View (Mermaid)

```mermaid
graph TD
  n0["PROGRAM"]
  n1["STATEMENT"]
  n2["STATEMENT"]
  n3["PRINT"]
  n4["ID\n[x]"]
  n5["DECLARATION"]
  n6["NUM\n[42]"]
  n7["ID\n[x]"]
  n8["TYPE\n[num]"]
  n0 --> n1
  n0 --> n2
  n2 --> n3
  n3 --> n4
  n2 --> n5
  n5 --> n6
  n5 --> n7
  n5 --> n8
```

### Exported Graph Files

- DOT: part3_graphs/testcases_valid_test1_basic.bro.dot
- PNG: part3_graphs/testcases_valid_test1_basic.bro.png

### Structured Reduction Trace

| Step | Depth | Symbol | Value |
|---:|---:|---|---|
| 1 | 3 | TYPE | num |
| 2 | 3 | ID | x |
| 3 | 3 | NUM | 42 |
| 4 | 2 | DECLARATION | - |
| 5 | 3 | ID | x |
| 6 | 2 | PRINT | - |
| 7 | 1 | STATEMENT | - |
| 8 | 1 | STATEMENT | - |
| 9 | 0 | PROGRAM | - |

## Testcase: testcases/valid/test2_if_else.bro

### Tree View (Post-Order)

```text
      └─ TYPE [num]
      └─ ID [a]
      └─ NUM [10]
    └─ DECLARATION
        └─ ID [a]
        └─ OP [>]
        └─ NUM [5]
      └─ BINOP
            └─ NUM [1]
          └─ PRINT
        └─ STATEMENT
      └─ BLOCK
              └─ NUM [2]
            └─ PRINT
          └─ STATEMENT
        └─ BLOCK
      └─ ELSE
    └─ IF
  └─ STATEMENT
  └─ STATEMENT
└─ PROGRAM
```

### Graph View (Mermaid)

```mermaid
graph TD
  n0["PROGRAM"]
  n1["STATEMENT"]
  n2["STATEMENT"]
  n3["IF"]
  n4["ELSE"]
  n5["BLOCK"]
  n6["STATEMENT"]
  n7["PRINT"]
  n8["NUM\n[2]"]
  n9["BLOCK"]
  n10["STATEMENT"]
  n11["PRINT"]
  n12["NUM\n[1]"]
  n13["BINOP"]
  n14["NUM\n[5]"]
  n15["OP\n[>]"]
  n16["ID\n[a]"]
  n17["DECLARATION"]
  n18["NUM\n[10]"]
  n19["ID\n[a]"]
  n20["TYPE\n[num]"]
  n0 --> n1
  n0 --> n2
  n2 --> n3
  n3 --> n4
  n4 --> n5
  n5 --> n6
  n6 --> n7
  n7 --> n8
  n3 --> n9
  n9 --> n10
  n10 --> n11
  n11 --> n12
  n3 --> n13
  n13 --> n14
  n13 --> n15
  n13 --> n16
  n2 --> n17
  n17 --> n18
  n17 --> n19
  n17 --> n20
```

### Exported Graph Files

- DOT: part3_graphs/testcases_valid_test2_if_else.bro.dot
- PNG: part3_graphs/testcases_valid_test2_if_else.bro.png

### Structured Reduction Trace

| Step | Depth | Symbol | Value |
|---:|---:|---|---|
| 1 | 3 | TYPE | num |
| 2 | 3 | ID | a |
| 3 | 3 | NUM | 10 |
| 4 | 2 | DECLARATION | - |
| 5 | 4 | ID | a |
| 6 | 4 | OP | > |
| 7 | 4 | NUM | 5 |
| 8 | 3 | BINOP | - |
| 9 | 6 | NUM | 1 |
| 10 | 5 | PRINT | - |
| 11 | 4 | STATEMENT | - |
| 12 | 3 | BLOCK | - |
| 13 | 7 | NUM | 2 |
| 14 | 6 | PRINT | - |
| 15 | 5 | STATEMENT | - |
| 16 | 4 | BLOCK | - |
| 17 | 3 | ELSE | - |
| 18 | 2 | IF | - |
| 19 | 1 | STATEMENT | - |
| 20 | 1 | STATEMENT | - |
| 21 | 0 | PROGRAM | - |

## Testcase: testcases/valid/test3_loop.bro

### Tree View (Post-Order)

```text
      └─ TYPE [num]
      └─ ID [i]
      └─ NUM [0]
    └─ DECLARATION
        └─ ID [i]
        └─ OP [<]
        └─ NUM [5]
      └─ BINOP
            └─ ID [i]
          └─ PRINT
            └─ ID [i]
            └─ OP [+=]
            └─ NUM [1]
          └─ ASSIGNMENT
        └─ STATEMENT
        └─ STATEMENT
      └─ BLOCK
    └─ WHILE
  └─ STATEMENT
  └─ STATEMENT
└─ PROGRAM
```

### Graph View (Mermaid)

```mermaid
graph TD
  n0["PROGRAM"]
  n1["STATEMENT"]
  n2["STATEMENT"]
  n3["WHILE"]
  n4["BLOCK"]
  n5["STATEMENT"]
  n6["STATEMENT"]
  n7["ASSIGNMENT"]
  n8["NUM\n[1]"]
  n9["OP\n[+=]"]
  n10["ID\n[i]"]
  n11["PRINT"]
  n12["ID\n[i]"]
  n13["BINOP"]
  n14["NUM\n[5]"]
  n15["OP\n[<]"]
  n16["ID\n[i]"]
  n17["DECLARATION"]
  n18["NUM\n[0]"]
  n19["ID\n[i]"]
  n20["TYPE\n[num]"]
  n0 --> n1
  n0 --> n2
  n2 --> n3
  n3 --> n4
  n4 --> n5
  n4 --> n6
  n6 --> n7
  n7 --> n8
  n7 --> n9
  n7 --> n10
  n6 --> n11
  n11 --> n12
  n3 --> n13
  n13 --> n14
  n13 --> n15
  n13 --> n16
  n2 --> n17
  n17 --> n18
  n17 --> n19
  n17 --> n20
```

### Exported Graph Files

- DOT: part3_graphs/testcases_valid_test3_loop.bro.dot
- PNG: part3_graphs/testcases_valid_test3_loop.bro.png

### Structured Reduction Trace

| Step | Depth | Symbol | Value |
|---:|---:|---|---|
| 1 | 3 | TYPE | num |
| 2 | 3 | ID | i |
| 3 | 3 | NUM | 0 |
| 4 | 2 | DECLARATION | - |
| 5 | 4 | ID | i |
| 6 | 4 | OP | < |
| 7 | 4 | NUM | 5 |
| 8 | 3 | BINOP | - |
| 9 | 6 | ID | i |
| 10 | 5 | PRINT | - |
| 11 | 6 | ID | i |
| 12 | 6 | OP | += |
| 13 | 6 | NUM | 1 |
| 14 | 5 | ASSIGNMENT | - |
| 15 | 4 | STATEMENT | - |
| 16 | 4 | STATEMENT | - |
| 17 | 3 | BLOCK | - |
| 18 | 2 | WHILE | - |
| 19 | 1 | STATEMENT | - |
| 20 | 1 | STATEMENT | - |
| 21 | 0 | PROGRAM | - |

## Testcase: testcases/valid/test4_arithmetic.bro

### Tree View (Post-Order)

```text
      └─ TYPE [num]
      └─ ID [x]
        └─ NUM [2]
        └─ OP [+]
          └─ NUM [3]
          └─ OP [*]
          └─ NUM [4]
        └─ BINOP
      └─ BINOP
    └─ DECLARATION
      └─ TYPE [num]
      └─ ID [y]
          └─ NUM [2]
          └─ OP [+]
          └─ NUM [3]
        └─ BINOP
        └─ OP [*]
        └─ NUM [4]
      └─ BINOP
    └─ DECLARATION
      └─ ID [y]
      └─ ID [x]
    └─ PRINT
  └─ STATEMENT
  └─ STATEMENT
  └─ STATEMENT
└─ PROGRAM
```

### Graph View (Mermaid)

```mermaid
graph TD
  n0["PROGRAM"]
  n1["STATEMENT"]
  n2["STATEMENT"]
  n3["STATEMENT"]
  n4["PRINT"]
  n5["ID\n[x]"]
  n6["ID\n[y]"]
  n7["DECLARATION"]
  n8["BINOP"]
  n9["NUM\n[4]"]
  n10["OP\n[*]"]
  n11["BINOP"]
  n12["NUM\n[3]"]
  n13["OP\n[+]"]
  n14["NUM\n[2]"]
  n15["ID\n[y]"]
  n16["TYPE\n[num]"]
  n17["DECLARATION"]
  n18["BINOP"]
  n19["BINOP"]
  n20["NUM\n[4]"]
  n21["OP\n[*]"]
  n22["NUM\n[3]"]
  n23["OP\n[+]"]
  n24["NUM\n[2]"]
  n25["ID\n[x]"]
  n26["TYPE\n[num]"]
  n0 --> n1
  n0 --> n2
  n0 --> n3
  n3 --> n4
  n4 --> n5
  n4 --> n6
  n3 --> n7
  n7 --> n8
  n8 --> n9
  n8 --> n10
  n8 --> n11
  n11 --> n12
  n11 --> n13
  n11 --> n14
  n7 --> n15
  n7 --> n16
  n3 --> n17
  n17 --> n18
  n18 --> n19
  n19 --> n20
  n19 --> n21
  n19 --> n22
  n18 --> n23
  n18 --> n24
  n17 --> n25
  n17 --> n26
```

### Exported Graph Files

- DOT: part3_graphs/testcases_valid_test4_arithmetic.bro.dot
- PNG: part3_graphs/testcases_valid_test4_arithmetic.bro.png

### Structured Reduction Trace

| Step | Depth | Symbol | Value |
|---:|---:|---|---|
| 1 | 3 | TYPE | num |
| 2 | 3 | ID | x |
| 3 | 4 | NUM | 2 |
| 4 | 4 | OP | + |
| 5 | 5 | NUM | 3 |
| 6 | 5 | OP | * |
| 7 | 5 | NUM | 4 |
| 8 | 4 | BINOP | - |
| 9 | 3 | BINOP | - |
| 10 | 2 | DECLARATION | - |
| 11 | 3 | TYPE | num |
| 12 | 3 | ID | y |
| 13 | 5 | NUM | 2 |
| 14 | 5 | OP | + |
| 15 | 5 | NUM | 3 |
| 16 | 4 | BINOP | - |
| 17 | 4 | OP | * |
| 18 | 4 | NUM | 4 |
| 19 | 3 | BINOP | - |
| 20 | 2 | DECLARATION | - |
| 21 | 3 | ID | y |
| 22 | 3 | ID | x |
| 23 | 2 | PRINT | - |
| 24 | 1 | STATEMENT | - |
| 25 | 1 | STATEMENT | - |
| 26 | 1 | STATEMENT | - |
| 27 | 0 | PROGRAM | - |

## Testcase: testcases/valid/test5_nested_if.bro

### Tree View (Post-Order)

```text
      └─ TYPE [bool]
      └─ ID [flag]
      └─ BOOL [sahi]
    └─ DECLARATION
      └─ ID [flag]
            └─ BOOL [sahi]
                  └─ NUM [1]
                └─ PRINT
              └─ STATEMENT
            └─ BLOCK
                    └─ NUM [2]
                  └─ PRINT
                └─ STATEMENT
              └─ BLOCK
            └─ ELSE
          └─ IF
        └─ STATEMENT
      └─ BLOCK
    └─ IF
  └─ STATEMENT
  └─ STATEMENT
└─ PROGRAM
```

### Graph View (Mermaid)

```mermaid
graph TD
  n0["PROGRAM"]
  n1["STATEMENT"]
  n2["STATEMENT"]
  n3["IF"]
  n4["BLOCK"]
  n5["STATEMENT"]
  n6["IF"]
  n7["ELSE"]
  n8["BLOCK"]
  n9["STATEMENT"]
  n10["PRINT"]
  n11["NUM\n[2]"]
  n12["BLOCK"]
  n13["STATEMENT"]
  n14["PRINT"]
  n15["NUM\n[1]"]
  n16["BOOL\n[sahi]"]
  n17["ID\n[flag]"]
  n18["DECLARATION"]
  n19["BOOL\n[sahi]"]
  n20["ID\n[flag]"]
  n21["TYPE\n[bool]"]
  n0 --> n1
  n0 --> n2
  n2 --> n3
  n3 --> n4
  n4 --> n5
  n5 --> n6
  n6 --> n7
  n7 --> n8
  n8 --> n9
  n9 --> n10
  n10 --> n11
  n6 --> n12
  n12 --> n13
  n13 --> n14
  n14 --> n15
  n6 --> n16
  n3 --> n17
  n2 --> n18
  n18 --> n19
  n18 --> n20
  n18 --> n21
```

### Exported Graph Files

- DOT: part3_graphs/testcases_valid_test5_nested_if.bro.dot
- PNG: part3_graphs/testcases_valid_test5_nested_if.bro.png

### Structured Reduction Trace

| Step | Depth | Symbol | Value |
|---:|---:|---|---|
| 1 | 3 | TYPE | bool |
| 2 | 3 | ID | flag |
| 3 | 3 | BOOL | sahi |
| 4 | 2 | DECLARATION | - |
| 5 | 3 | ID | flag |
| 6 | 6 | BOOL | sahi |
| 7 | 9 | NUM | 1 |
| 8 | 8 | PRINT | - |
| 9 | 7 | STATEMENT | - |
| 10 | 6 | BLOCK | - |
| 11 | 10 | NUM | 2 |
| 12 | 9 | PRINT | - |
| 13 | 8 | STATEMENT | - |
| 14 | 7 | BLOCK | - |
| 15 | 6 | ELSE | - |
| 16 | 5 | IF | - |
| 17 | 4 | STATEMENT | - |
| 18 | 3 | BLOCK | - |
| 19 | 2 | IF | - |
| 20 | 1 | STATEMENT | - |
| 21 | 1 | STATEMENT | - |
| 22 | 0 | PROGRAM | - |

## Testcase: testcases/valid/test6_constants.bro

### Tree View (Post-Order)

```text
      └─ TYPE [num]
      └─ ID [PI]
      └─ NUM [3]
    └─ CONSTANT_DECL
      └─ TYPE [str]
      └─ ID [MSG]
      └─ STR ["hello"]
    └─ CONSTANT_DECL
      └─ ID [MSG]
      └─ ID [PI]
    └─ PRINT
  └─ STATEMENT
  └─ STATEMENT
  └─ STATEMENT
└─ PROGRAM
```

### Graph View (Mermaid)

```mermaid
graph TD
  n0["PROGRAM"]
  n1["STATEMENT"]
  n2["STATEMENT"]
  n3["STATEMENT"]
  n4["PRINT"]
  n5["ID\n[PI]"]
  n6["ID\n[MSG]"]
  n7["CONSTANT_DECL"]
  n8["STR\n['hello']"]
  n9["ID\n[MSG]"]
  n10["TYPE\n[str]"]
  n11["CONSTANT_DECL"]
  n12["NUM\n[3]"]
  n13["ID\n[PI]"]
  n14["TYPE\n[num]"]
  n0 --> n1
  n0 --> n2
  n0 --> n3
  n3 --> n4
  n4 --> n5
  n4 --> n6
  n3 --> n7
  n7 --> n8
  n7 --> n9
  n7 --> n10
  n3 --> n11
  n11 --> n12
  n11 --> n13
  n11 --> n14
```

### Exported Graph Files

- DOT: part3_graphs/testcases_valid_test6_constants.bro.dot
- PNG: part3_graphs/testcases_valid_test6_constants.bro.png

### Structured Reduction Trace

| Step | Depth | Symbol | Value |
|---:|---:|---|---|
| 1 | 3 | TYPE | num |
| 2 | 3 | ID | PI |
| 3 | 3 | NUM | 3 |
| 4 | 2 | CONSTANT_DECL | - |
| 5 | 3 | TYPE | str |
| 6 | 3 | ID | MSG |
| 7 | 3 | STR | "hello" |
| 8 | 2 | CONSTANT_DECL | - |
| 9 | 3 | ID | MSG |
| 10 | 3 | ID | PI |
| 11 | 2 | PRINT | - |
| 12 | 1 | STATEMENT | - |
| 13 | 1 | STATEMENT | - |
| 14 | 1 | STATEMENT | - |
| 15 | 0 | PROGRAM | - |

