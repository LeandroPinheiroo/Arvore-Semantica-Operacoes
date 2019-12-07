# coding: utf-8

################################################################################################
# João Paulo de Souza    - 0035329                                                             #
# Leandro Souza Pinheiro - 0015137                                                             #
# Trabalho Compiladores  - Trabalho sobre geração de árvore semântica para linguagem pos fixa  #
# Data: 09/12/2019                                                                             #
################################################################################################

# classe do node
class Node:
    def __init__(self, data):
        # atributos da cada no da arvore
        self.left = None
        self.right = None
        self.data = data

# classe da arvore binaria
class Tree:
    # construtor
    def __init__(self):
        pass

    # metodo para verificar se o caractere e um operador 
    def isOperator(self, c): 
        if (c == '+' or c == '-' or c == '*'
            or c == '/'): 
            return True
        else: 
            return False
    
    # método para preencher a fila em pos ordem 
    def postOrder(self, root, queue): 
        if root is not None:
            self.postOrder(root.left, queue)  
            self.postOrder(root.right, queue)
            queue.append(root.data)
    

    # método para gerar a arvore a partir da expressao 
    def generateTree(self, expression): 
        # utiliza uma pilha para auxiliar
        stack = [] 
        # le caractere a caractere da expressão 
        for char in expression : 
            # se não for operador, então empilha o no 
            if not self.isOperator(char): 
                n = Node(char) 
                stack.append(n) 
            # Operator 
            else: 
                # caso for um operador, desempilha os valores
                n = Node(char) 
                t1 = stack.pop() 
                t2 = stack.pop()  
                # monta o no 
                n.right = t1 
                n.left = t2 
                # depois adiciona o no na pilha 
                stack.append(n) 
        # no fim retona o no raiz 
        t = stack.pop() 
        return t 
