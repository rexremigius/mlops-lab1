import pytest
from src import calculator 
def test_sqrt():
    assert calculator.sqrt(4) == 2
    assert calculator.sqrt(0) == 0

def test_degree_to_radian():
    assert calculator.degree_to_radian(180) == pytest.approx(3.14159)
    assert calculator.degree_to_radian(0) == 0
    
def test_radian_to_degree():
    assert calculator.radian_to_degree(3.14159) == pytest.approx(180)
    assert calculator.radian_to_degree(0) == 0

def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(10, 2) == 100
