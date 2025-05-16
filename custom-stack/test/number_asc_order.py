import pytest
from unittest.mock import MagicMock, patch
from src.custom_stack_class import *
from src.number_asc_order import NumberAscOrder

class TestNumberAscOrder:

    @patch('random.sample')
    def test_sort_with_six_numbers(self, mock_random_sample):
        """Testa com uma pilha contendo 6 números sorteados usando mock"""
        fixed_numbers = [10, 30, 20, 50, 40, 60]
        mock_random_sample.return_value = fixed_numbers
        
        stack_items = fixed_numbers.copy()
        
        stack_mock = MagicMock(spec=CustomStack)
        stack_mock.size.return_value = 6
        stack_mock.is_empty.side_effect = lambda: len(stack_items) == 0
        stack_mock.pop.side_effect = lambda: stack_items.pop()
        
        sorter = NumberAscOrder()
        sorted_numbers = sorter.sort(stack_mock)
        
        assert len(sorted_numbers) == 6
        assert sorted_numbers == sorted(fixed_numbers)
        assert stack_mock.is_empty.call_count >= 6

    def test_sort_empty_stack(self):
        """Testa com uma pilha vazia usando mock"""
        stack_mock = MagicMock(spec=CustomStack)
        stack_mock.is_empty.return_value = True
        stack_mock.pop.side_effect = StackEmptyException("A pilha está vazia")
        
        sorter = NumberAscOrder()
        
        with pytest.raises(StackEmptyException) as excinfo:
            sorter.sort(stack_mock)
            
        assert "A pilha está vazia" in str(excinfo.value)
        stack_mock.is_empty.assert_called_once()

    def test_sort_verify_order(self):
        """Verifica se a ordenação está correta"""
        test_numbers = [10, 5, 20, 15, 25, 1]
        expected = sorted(test_numbers)
        
        stack_items = test_numbers.copy()
        
        stack_mock = MagicMock(spec=CustomStack)
        stack_mock.size.return_value = 6
        stack_mock.is_empty.side_effect = lambda: len(stack_items) == 0
        stack_mock.pop.side_effect = lambda: stack_items.pop()  # Remove do final (comportamento LIFO)
        
        sorter = NumberAscOrder()
        result = sorter.sort(stack_mock)
        
        assert result == expected
        assert result[0] == 1
        assert result[-1] == 25
        assert len(result) == 6