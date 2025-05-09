import pytest
from src.custom_stack_class import *
from src.number_asc_order import NumberAscOrder
import random

class TestNumberAscOrder:

    def test_sort_with_six_numbers(self):
        """Testa com uma pilha contendo 6 números sorteados"""
        stack = CustomStack(6)
        numbers = random.sample(range(1, 61), 6)
        
        for num in numbers:
            stack.push(num)
            
        sorter = NumberAscOrder()
        sorted_numbers = sorter.sort(stack)
        
        assert len(sorted_numbers) == 6
        assert sorted_numbers == sorted(numbers)
        assert stack.is_empty()

    def test_sort_empty_stack(self):
        """Testa com uma pilha vazia"""
        stack = CustomStack(6)
        sorter = NumberAscOrder()
        
        with pytest.raises(StackEmptyException) as excinfo:
            sorter.sort(stack)
            
        assert "A pilha está vazia" in str(excinfo.value)
        assert stack.is_empty()

    def test_sort_verify_order(self):
        """Verifica se a ordenação está correta"""
        stack = CustomStack(6)
        test_numbers = [10, 5, 20, 15, 25, 1]
        expected = sorted(test_numbers)
        
        for num in test_numbers:
            stack.push(num)
            
        sorter = NumberAscOrder()
        result = sorter.sort(stack)
        
        assert result == expected
        assert result[0] == 1
        assert result[-1] == 25
        assert len(result) == 6