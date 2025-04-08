#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for the main.py functions
"""
import pytest
from main import greet, calculate_sum, multiply


# Basit test fonksiyonu
def test_greet():
    """Test the greet function"""
    assert greet("Tunay") == "Hello, Tunay! Welcome to the PyCharm Git Integration project."
    assert greet("World") == "Hello, World! Welcome to the PyCharm Git Integration project."


# Parametreli test örneği
@pytest.mark.parametrize("a, b, expected", [(5, 7, 12), (-3, 3, 0), (0, 0, 0)])
def test_calculate_sum(a, b, expected):
    """Test the calculate_sum function with parameters"""
    assert calculate_sum(a, b) == expected


# Fixture kullanımı
@pytest.fixture
def sample_numbers():
    return {"a": 4, "b": 3, "product": 12}


def test_multiply_with_fixture(sample_numbers):
    """Test the multiply function using a fixture"""
    assert multiply(sample_numbers["a"], sample_numbers["b"]) == sample_numbers["product"]


# Normal test fonksiyonu
def test_multiply():
    """Test the multiply function"""
    assert multiply(4, 3) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 10) == 0