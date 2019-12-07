# coding: utf-8

################################################################################################
# João Paulo de Souza    - 0035329                                                             #
# Leandro Souza Pinheiro - 0015137                                                             #
# Trabalho Compiladores  - Trabalho sobre geração de árvore semântica para linguagem pos fixa  #
# Data: 09/12/2019                                                                             #
################################################################################################

from Tree import Tree
from Operation import Operation
import sys
import os

def main():
    path = sys.argv[1]
    if not os.path.exists(path):
        print("Por favor passe o caminho do arquivo!")
        return
    file = open(path, 'r')
    expression = file.readline() 
    stack = []
    tree = Tree() 
    t = tree.generateTree(expression) 
    queue = []
    tree.postOrder(t, queue)
    print(queue)
    op = Operation(t)
    print("Resultado e: " + str(op.solve()))

main()


