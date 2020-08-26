# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In busca.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""
from lib.searchProblem import SearchProblem

import lib.util as util
from lib.util import Stack, Queue, PriorityQueue
'''
Uso da pilha:
stack = Stack()
stack.push(element)
l = stack.list # Lista de elementos na pilha
e = stack.pop()

Uso da fila:
queue = Queue()
queue.push(element)
l = queue.list # Lista de elementos na fila
e = queue.pop()

Uso da fila de prioridades:
queuep = PriorityQueue()
queuep.push(element, value) # Valores baixos indicam maior prioridade
queuep.update(element, value) # Atualiza o valor de prioridade  de um elemento
l = queuep.heap # Lista de elementos na fila
e = queuep.pop()
'''

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):

    # Seu algoritmo deve retornar uma lista de acoes que atinja o objetivo.
    # "*** YOUR CODE HERE ***"
    familia = {}
    caminho = []
    fronteira = Stack()
    visitados = set()

    atual = problem.getStartState() 
    fronteira.push(atual)

    while fronteira.list:

        atual = fronteira.pop()
        if problem.isGoalState(atual):
            temp = atual
            while familia.has_key(temp):
                caminho.insert(0, familia[temp][1]) # monta o caminho a partir do Goal, verificando quem faz parte da familia dele Dicionario = { Id_goal: [pai do goal, acao pai->goal]}
                temp = familia[temp][0] #pega quem era o pai do atual e verifica se ele tem um antecedente.
            return caminho

        visitados.add(atual)
        filhos = problem.getSuccessors(atual)
        for filho in filhos:
            if filho[0] not in visitados:
                familia[filho[0]] = [atual,filho[1]] # Fam = {B: [A,B-
                fronteira.push(filho[0])

    return []
    # print problem.getStartState()
    
    # print problem.isGoalState(problem.getStartState())
    # print problem.getSuccessors(problem.getStartState())


def breadthFirstSearch(problem):

    familia = {} #vai servir de guia para o caminho final da solucao
    caminho = []
    fronteira = [] # sao os nodos que estao atualmente na rodada para testar 
    visitados = set() # vai guardar quem ja foi testado, vai servir como base pra ajudar a ver qual ainda falta testar da fronteira set ()?
    
    # apos testado vai ser removido da fronteira e colocado em testados, antes disso vai expandir e colocar os filhos no final da lista de fronteira.
    atual = problem.getStartState()
    fronteira.append(atual) #primeiro a ter que ser testado
    
    while fronteira:

        atual = fronteira.pop(0) #pega o primeiro elemento que supostamente estava na mesma altura do anterior ou representa o primeiro elemento da proxima altura
        
        if problem.isGoalState(atual):

            temp = atual
            while familia.has_key(temp):
                caminho.insert(0,familia[temp][1]) # { G: [A, A->G] }
                temp = familia[temp][0]
            return caminho

        if atual not in visitados:
            visitados.add(atual)
            filhos = problem.getSuccessors(atual)
        
            for filho in filhos:
                if filho[0] not in fronteira:
                    if filho[0] not in visitados:
                        familia[filho[0]] = [atual,filho[1]] # G = [A, A->G] 
                        fronteira.append(filho[0])



    "*** YOUR CODE HERE ***"
    return []

def uniformCostSearch(problem):

    familia = {} #vai servir de guia para o caminho final da solucao
    caminho = []
    fronteira = PriorityQueue() # sao os nodos que estao atualmente na rodada para testar 
    visitados = set() # vai guardar quem ja foi testado, vai servir como base pra ajudar a ver qual ainda falta testar da fronteira

    atual = problem.getStartState()
    fronteira.push(atual,0.0) # ja que e o inicial, tomarei como sendo o menor custo possivel 
    peso_a = 0.0


    while fronteira.heap:
        atual = fronteira.pop()

        if familia.has_key(atual):
            peso_a = familia[atual][2]

        if problem.isGoalState(atual):
            temp = atual
            while familia.has_key(temp):
                caminho.insert(0,familia[temp][1])
                temp = familia[temp][0]
            return caminho

        if atual not in visitados:
            visitados.add(atual)
            filhos = problem.getSuccessors(atual)             


            for filho in filhos:
                if filho[0] not in visitados:
                    flag = 0
                    for i in fronteira.heap:
                        if filho[0] == i[2]: 
                            flag = 1 #sifnifica que estava na fronteira
                    
                    if flag == 0: # nao estava na fronteira, vou adicionar        
                        familia[filho[0]] = [atual,filho[1], (peso_a + filho[2]) ] #guarda o peso dele tb
                        fronteira.push(filho[0], (peso_a + filho[2]) ) # [A, peso]

                    elif flag == 1: #tava na fronteira, vou verificar custo
                        if (filho[2] + peso_a) <= familia[filho[0]][2]: #peso e o peso daquele filho                
                            familia[filho[0]] = [atual,filho[1], (peso_a + filho[2]) ]
                            fronteira.update(filho[0],(peso_a + filho[2]) )


    "*** YOUR CODE HERE ***"
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Busca primeiro os nos que tem a menor combinacao de custo total e heuristica"""
    "*** YOUR CODE HERE ***"
    familia = {} #vai servir de guia para o caminho final da solucao
    caminho = []
    fronteira = PriorityQueue() # sao os nodos que estao atualmente na rodada para testar 
    visitados = set() # vai guardar quem ja foi testado, vai servir como base pra ajudar a ver qual ainda falta testar da fronteira set ()?

    atual = problem.getStartState()
    fronteira.push(atual, 0 + heuristic(atual,problem) ) # ja que e o inicial, tomarei como sendo o menor custo possivel 
    peso_a = 0
    
    while fronteira.heap:
        atual = fronteira.pop()

        if familia.has_key(atual):
            peso_a = familia[atual][2] 

        if problem.isGoalState(atual):
            temp = atual
            while familia.has_key(temp):
                caminho.insert(0,familia[temp][1])
                temp = familia[temp][0]
            return caminho

        if atual not in visitados:
            visitados.add(atual)
            filhos = problem.getSuccessors(atual)             


            for filho in filhos:
                if filho[0] not in visitados:
                    flag = 0
                    for i in fronteira.heap:
                        if filho[0] == i[2]: 
                            flag = 1 #significa que estava na fronteira
                    
                    if flag == 0: # nao estava na fronteira, vou adicionar        
                        familia[filho[0]] = [atual,filho[1], (peso_a + filho[2] ) ] #guarda o peso dele tb
                        fronteira.push(filho[0], (peso_a + filho[2] + heuristic(filho[0],problem) ) ) # [A, peso]

                    elif flag == 1: #tava na fronteira, vou verificar custo
                        if (filho[2] + peso_a + heuristic(filho[0],problem)) <= familia[filho[0]][2]: #peso e o peso daquele filho                
                            familia[filho[0]] = [atual,filho[1], (peso_a + filho[2] ) ]
                            fronteira.update(filho[0],(peso_a + filho[2] + heuristic(filho[0],problem)) )



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
