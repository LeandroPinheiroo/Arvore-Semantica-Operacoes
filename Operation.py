# coding: utf-8

################################################################################################
# João Paulo de Souza    - 0035329                                                             #
# Leandro Souza Pinheiro - 0015137                                                             #
# Trabalho Compiladores  - Trabalho sobre geração de árvore semântica para linguagem pos fixa  #
# Data: 09/12/2019                                                                             #
################################################################################################

from Tree import Tree

# classe de operação
class Operation:
    # construtor que cria a fila, pila auxiliar e recebe no raiz da arvore
    def __init__(self, tree):
        self.queue = []
        self.tree = tree
        self.stack = []
    
    # método para resolver a expressão
    def solve(self):
        # instancia classe de arvore
        t = Tree()
        # preenche a fila com pos ordem
        t.postOrder(self.tree, self.queue)
        # caminha na fila 
        for i in self.queue:
            # verifica se é um operador
            if t.isOperator(i):
                # se for empilha ele
                self.stack.append(i)
                # e faz a operação
                self.verifyOperation()
            else:
                # senão, apenas empilha
                self.stack.append(i)
        # no fim retorna o resultado
        return self.stack[0]

    # método para realizar a operação
    def verifyOperation(self):
        size = len(self.stack)
        # verifica a operação e faz o calculo de acordo e 
        # empilha o valor resultante
        if self.stack[size - 1] == '+':
            x = int(self.stack[size - 3]) + int(self.stack[size - 2])
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            self.stack.append(x)
        elif self.stack[size - 1] == '-':
            x = int(self.stack[size - 3]) - int(self.stack[size - 2])
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            self.stack.append(x)
        elif self.stack[size - 1] == '*':
            x = int(self.stack[size - 3]) * int(self.stack[size - 2])
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            self.stack.append(x)
        elif self.stack[size - 1] == '/':
            x = int(self.stack[size - 3]) / int(self.stack[size - 2])
            self.stack.pop()
            self.stack.pop()
            self.stack.pop()
            self.stack.append(x)