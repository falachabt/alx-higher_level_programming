# Project Title

## Description

Welcome to the Python world! This project focuses on introducing you to Python programming with tasks that cover fundamental concepts. The initial projects have a "C-oriented" approach, making them simple and straightforward.

## Learning Objectives

- Understand why Python programming is awesome
- Learn about the creator of Python, Guido van Rossum
- Explore the Zen of Python and its principles
- Familiarize yourself with Python basics such as the Python interpreter, printing, strings, indexing, and slicing
- Follow the official Python coding style (PEP8) and use pycodestyle for code checking

## Resources

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP8 - Style Guide for Python Code](https://pep8.org/)
- [The Zen of Python](https://www.python.org/dev/peps/pep-0020/)

## Requirements

### Python Scripts

- Editors: vi, vim, emacs
- Python version: 3.8.5
- File format: All files end with a new line
- Shebang: `#!/usr/bin/python3`
- README.md: Mandatory at the root of the repository
- Code style: pycodestyle (version 2.8.*)
- Executability: All files must be executable
- Length: File length will be tested using `wc`
  
### Shell Scripts

- Editors: vi, vim, emacs
- Tested on: Ubuntu 20.04 LTS
- File format: All files end with a new line
- Shebang: `#!/bin/bash`
- Executability: All files must be executable
- Length: Exactly two lines long (`wc -l file` should print 2)

### C Scripts

- Editors: vi, vim, emacs
- Compiled on: Ubuntu 20.04 LTS using gcc with options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- File format: All files end with a new line
- Code style: Betty style
- Global variables: Not allowed
- Functions: No more than 5 functions per file
- Prototypes: Included in the header file (lists.h)
- Header files: Include guarded and pushed

