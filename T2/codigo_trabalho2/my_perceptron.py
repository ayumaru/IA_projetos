import numpy as np

"""
Da lista de exercicios
y = +1 se w.f(x) >= 0
y = 0 se w.f(x) < 0
se correto
erro = label - y 
-> Se 0 nao esta errada a classificação
Se 1, entao recalcula o vetor de pesos e o bias
Novo peso = peso antigo + Valor do erro * Vetor de peso com erro
novo bias =  bias antigo + erro
"""


def run_perceptron(weights, data, labels, learning_rate=1):

    epoch_error = 0
    erro = 0
    # wights [ bias, w1, w2]
    # Para cada instancia e label
    for x, y in zip(data, labels): # cada rodada executada representa 1 epoca
        # IMPLEMENTE AQUI A ATUALIZACAO DOS PESOS
        rest = np.dot(x,weights) # y = peso * w + bias

        if rest > 0:
            y_flag = 1
        else:
            y_flag = 0
       
        erro = y - y_flag # label - y

        if erro != 0:
            bias = weights[0]
            weights = weights + learning_rate*(erro*x) # novo peso 
            weights[0] = (bias + erro)*learning_rate
            epoch_error+=1

        #pass

    return weights, epoch_error