import pytest
from src.custom_stack_class import *

def test_push_one_element_in_stack():
    element_value = 5.0
    
    cut = CustomStack(5)
    cut.push(element_value)
    assert cut.is_empty() == False
    assert element_value == cut.top()
    assert 1 == cut.size()

def test_push_multiple_elements():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    cut.push(3)
    
    assert cut.is_empty() == False
    assert 3 == cut.top()
    assert 3 == cut.size()

def test_pop_element():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    
    assert 2 == cut.pop()
    assert 1 == cut.size()
    assert 1 == cut.top()

def test_pop_last_element():
    cut = CustomStack(3)
    cut.push(1)
    
    assert 1 == cut.pop()
    assert 0 == cut.size()
    assert cut.is_empty()

def test_top_without_removing():
    cut = CustomStack(3)
    cut.push(1)
    cut.push(2)
    
    assert 2 == cut.top()
    assert 2 == cut.size()

def test_stack_empty_exception_on_pop():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.pop()

def test_stack_empty_exception_on_top():
    cut = CustomStack(3)
    with pytest.raises(StackEmptyException):
        cut.top()

def test_stack_full_exception():
    cut = CustomStack(2)
    cut.push(1)
    cut.push(2)
    
    with pytest.raises(StackFullException):
        cut.push(3)

def test_interleaved_push_pop():
    cut = CustomStack(5)
    cut.push(1)
    cut.push(2)
    assert 2 == cut.pop()  # Remove o último elemento (2)
    
    cut.push(3)
    assert 3 == cut.top()  # Topo agora é 3
    assert 2 == cut.size()  # Temos [1, 3]
    
    # O próximo pop() deve remover 3 (último adicionado)
    assert 3 == cut.pop()
    
    # Agora só resta o 1
    assert 1 == cut.pop()
    
    # Stack vazia
    assert cut.is_empty()