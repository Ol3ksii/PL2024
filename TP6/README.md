# TPC6

**Author**: [**A102131** Oleksii Tantsura](https://www.github.com/Ol3ksii)

**Date**: 2025-04-01

## Summary

In this task (TPC6), the goal is to implement a recursive descent parser using **PLY** that evaluates arithmetic expressions.

The parser supports expressions involving:

- **Binary operators**: `+`, `-`, `*`, `/`
- **Integer numbers**
- **Parentheses** to enforce precedence

The implementation is split into two files:
- `exp_analex.py`: defines lexical analysis (tokenizer)
- `exp_anasin.py`: defines parsing rules and evaluation logic

## Results

The program is executed from the command line and reads expressions from standard input. Example usage:

```bash
python3 exp_anasin.py
```

### Input:
```
67-(2+3*4)
2+3
(9-2)*(13-4)
```

### Output:
```
Generating LALR tables
67-(2+3*4)
Result: 53
2+3
Result: 5
(9-2)*(13-4)
Result: 63
```

- **1** (Addition and Subtraction):
    - Supports chained operations and correct precedence resolution.

- **2** (Multiplication and Division):
    - Evaluated before addition/subtraction according to standard arithmetic rules.

- **3** (Parentheses):
    - Forces precedence for grouped expressions.

- **4** (Error handling):
    - Invalid syntax is caught and reported cleanly.

## Conclusion

The parser reads arithmetic expressions, constructs and evaluates them according to operator precedence and grouping. Using PLY enables a structured implementation suitable for LL(1) recursive descent parsing.
