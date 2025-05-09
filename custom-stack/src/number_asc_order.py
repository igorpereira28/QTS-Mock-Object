from src.custom_stack_class import CustomStack, StackEmptyException

class NumberAscOrder:
    
    def sort(self, custom_stack):
        """
        Ordena os números de uma CustomStack em ordem ascendente
        
        Args:
            custom_stack: CustomStack contendo os números a serem ordenados
            
        Returns:
            list: Lista ordenada em ordem ascendente
            
        Raises:
            StackEmptyException: Se a pilha estiver vazia
        """
        if custom_stack.is_empty():
            raise StackEmptyException("A pilha está vazia")
            
        numbers = []
        while not custom_stack.is_empty():
            numbers.append(custom_stack.pop())
            
        numbers.sort()
        return numbers