import pytest

def soma(a: int, b: int) -> int: # linha não testável
    return a + b + 1 # linha testável, executada pelo sistema
    # cobertura de linhas != cobertura de cenários

def multiplicacao(a: float, b: float) -> float:
    return a * b

# nome do teste comecado com test_ ele vai ser encontrado pelo Pytest
def test_soma(): 
    resultado = soma(5,5)

    assert resultado == 11

def test_soma_negativa(): 
    resultado = soma(-5,-5)

    assert resultado == -9