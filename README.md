# QTS-Mock-Object
Atividade de qualidade e testes de software

Atividade solicitada:
Exercício Prático - Mock Object

Assumindo o projeto custom-stack.zip disponibilizado na semana de aula, faça:

Preparo do Ambiente

Crie uma venv na raiz do projeto
Instale as dependêncas contidas no arquivo requirements.txt
Mais detalhes, consulte https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/ 
Part 1

Implementar os testes de unidade da classe CustomStack desenvolvida de forma que a cobertura seja igual a 100% (usar ferramentas como o pytest-cov para analisar a cobertura).

Obervação: Atualmente está em 79%, porém é necessário analisar a efetividade do teste existente.

Parte 2

A equipe da Caixa Econômica Federal, tem como objetivo desenvolver uma classe com responsabilidade de coletar todos os número sorteados da Mega Sena que estarão armazenados em um objeto CustomStack, conforme ordem do sorteio realizado, e ordená-los de forma ascendente.

Para tal o objetivo é implementar:

Um classe chamada NumberAscOrder
Um método denominado sort() (que recebe uma CustomStack como parâmetro) que deverá retornar um list() ordenado, bem como os devidos tratamentos/verificações necessários
Uma classe de teste com os casos de teste necessários para atender os seguintes cenários
Uma pilha de 6 posições, contendo os 6 números sorteados (aleatoriamente)
Uma pilha de 6 posições, vazia
Observação:

O projeto dever ser desenvolvido em Python (usando pytest/pytest-mock ou unittest/unittest-mock)
Nenhum método adicional deve ser criado nas classes já existentes no projeto
