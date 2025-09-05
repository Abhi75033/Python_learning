# Comprehensive Python Notes 🐍

A detailed guide covering the fundamental concepts of Python, from basic data types to file handling. This document is designed for learners and as a quick reference for developers.

---

## Table of Contents

* [Typecasting](#typecasting)
* [Strings](#strings-📜)
    * [Slicing in Strings](#slicing-in-strings)
    * [String Methods](#string-methods)
    * [Escape Characters](#escape-characters)
    * [String Formatting](#string-formatting-techniques)
* [Lists and Tuples](#lists-and-tuples)
    * [Lists](#lists-️)
    * [Tuples](#tuples-️)
* [Dictionaries and Sets](#dictionaries-and-sets)
    * [Dictionaries](#dictionaries-)
    * [Sets](#sets-️)
* [Control Flow](#control-flow)
    * [Conditional Statements](#conditional-statements)
    * [Looping](#looping-)
    * [Loop Control Keywords](#loop-control-keywords-break-continue--pass)
* [Operators](#operators-in-python)
* [Functions and Recursion](#functions-and-recursion)
    * [Functions](#functions-)
    * [Recursion](#recursion-)
* [File I/O](#file-io-)

---

## Typecasting

In Python, you cannot perform operations between incompatible data types, such as adding a string to an integer. To resolve this, you must explicitly convert one data type to another, a process known as **typecasting**.

**Example: String + Integer**

```python
a = "Abhishek got marks: "
b = 228

# print(a + b) # This will raise a TypeError

# Correct way: Typecast the integer 'b' to a string
print(a + str(b))
# Output: Abhishek got marks: 228

