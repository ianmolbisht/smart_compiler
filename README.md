# Smart Static Code Analyzer & Optimization Engine

An advanced **AI-ready static code analysis platform** for C-like languages built using **Python**, **Flask**, compiler design principles, and modern visualization techniques.

The project performs:

* Lexical Analysis
* Recursive Descent Parsing
* AST Generation & Visualization
* Semantic Analysis
* Symbol Table Management
* Static Code Quality Analysis
* Compiler Diagnostics
* Optimization Suggestions
* Dead Code Elimination
* Constant Folding
* Algebraic Simplification

---

# Features

## Compiler Pipeline

```text
Source Code
   ↓
Lexer
   ↓
Parser
   ↓
Abstract Syntax Tree (AST)
   ↓
Semantic Analyzer
   ↓
Optimization Engine
   ↓
Visualization & Metrics
```

---

# Core Functionalities

## 1. Lexical Analysis

Converts source code into tokens.

Supported token types:

* Keywords
* Identifiers
* Numbers
* Operators
* Symbols
* Preprocessor directives

---

## 2. Recursive Descent Parser

Implements a custom parser for a C-like language grammar.

Supports:

* Variable declarations
* Assignments
* Arithmetic expressions
* Functions
* Return statements
* Nested blocks

---

## 3. AST Generation

Builds an Abstract Syntax Tree representing the parsed code structure.

Features:

* Interactive AST visualization
* Zoom & pan support
* Expand/collapse nodes
* Hierarchical tree rendering

---

## 4. Semantic Analysis

Performs static semantic checks including:

* Undeclared variable detection
* Duplicate declarations
* Scope management
* Unused variable detection
* Unreachable code detection

---

## 5. Symbol Table

Tracks:

* Variable declarations
* Scope levels
* Usage state
* Assignment state

---

## 6. Optimization Engine

Implements compiler optimization techniques.

### Constant Folding

```c
int x = 5 + 3;
```

↓

```c
int x = 8;
```

---

### Algebraic Simplification

```c
x = y + 0;
```

↓

```c
x = y;
```

---

### Dead Code Elimination

```c
return y;
printf("dead");
```

↓

```c
return y;
```

---

# GCC Integration

Uses GCC for real compiler diagnostics.

Displays:

* Compiler errors
* Warnings
* Exit codes
* GCC output logs

---

# pycparser Integration

Parses full C syntax using pycparser for comparison and validation.

---

# Metrics Dashboard

Displays:

* Token distribution
* AST depth
* Function count
* Variable count
* Code quality score

---

# Technology Stack

## Backend

* Python
* Flask

## Compiler Components

* Recursive Descent Parser
* Custom Lexer
* AST Engine
* Semantic Analyzer

## Frontend

* HTML
* CSS
* Vanilla JavaScript
* SVG AST Visualization

## External Tools

* GCC
* pycparser

---

# Project Structure

```text
smart_static_analyzer/
│
├── analyzer/
│   ├── ast_parser.py
│
├── compiler/
│   ├── compile_checker.py
│
├── optimizer/
│   ├── __init__.py
│   ├── optimizer.py
│   ├── rules.py
│   └── transforms.py
│
├── semantic/
│   ├── analyzer.py
│   ├── quality_scorer.py
│
├── static/
│   ├── style.css
│
├── templates/
│   ├── index.html
│
├── app.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── utils.py
│
└── requirements.txt
```

---

# Supported Language Features

## Variable Declaration

```c
int x;
```

---

## Assignment

```c
x = 10;
x = y + 5;
```

---

## Functions

```c
int main() {
    return 0;
}
```

---

## Blocks

```c
{
    int x;
    x = 5;
}
```

---

# Running the Project

## Clone Repository

```bash
git clone <your-repo-url>
cd smart_static_analyzer
```

---

## Install Dependencies

```bash
pip install flask pycparser
```

---

## Run Application

```bash
python app.py
```

---

## Open in Browser

```text
http://127.0.0.1:5000
```

---

# API Endpoint

## POST /analyze

### Request

```json
{
  "code": "int x = 5 + 3;"
}
```

---

### Response

```json
{
  "tokens": [],
  "ast": {},
  "optimized_ast": {},
  "optimizations": [],
  "semantic": {},
  "metrics": {},
  "errors": []
}
```

---

# Example Optimization Output

## Input

```c
int main() {

    int x = 5 + 3;

    int y = x + 0;

    return y;

    printf("dead code");
}
```

---

## Optimization Suggestions

```text
Constant Folding:
5 + 3 → 8

Algebraic Simplification:
x + 0 → x

Dead Code Elimination:
printf removed
```

---

# Future Improvements

* Control Flow Graph (CFG)
* Cyclomatic Complexity Analysis
* Data Flow Analysis
* Intermediate Representation (IR)
* Loop Optimization
* AI-Powered Refactoring
* CodeBERT Integration
* Complexity Prediction
* Automatic Code Repair

---

# Educational Concepts Demonstrated

* Compiler Design
* Formal Grammars
* Recursive Descent Parsing
* Abstract Syntax Trees
* Semantic Analysis
* Static Analysis
* Compiler Optimization
* Symbol Tables
* Code Visualization

---

# Use Cases

* Compiler Design Learning
* Static Code Analysis
* Developer Tooling
* Educational Visualization
* Optimization Demonstration
* AI-assisted Code Intelligence Research

---

# Author

Anmol Bisht
Pratishtha Goyal
Akshat Kumar
Janhavi Negi

---

# License

MIT License
