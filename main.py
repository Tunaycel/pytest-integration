#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main module for the PyCharm Git Integration Project
Author: Huseyin Tunay Celik
"""

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}! Welcome to the PyCharm Git Integration project."

def calculate_sum(a, b):
    """Calculate the sum of two numbers"""
    return a + b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def main():
    """Main function to demonstrate the application"""
    print(greet("User"))
    print(f"The sum of 5 and 7 is: {calculate_sum(5, 7)}")
    print(f"The product of 4 and 3 is: {multiply(4, 3)}")
    print("This project demonstrates Git integration in PyCharm")

if __name__ == "__main__":
    main()