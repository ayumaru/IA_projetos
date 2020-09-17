import random
import numpy as np

class QLearningAgent():
    def __init__(self, env, epsilon=0.01, alpha=0.8, gamma=0.2):
        self.epsilon = epsilon # exploration
        self.alpha = alpha   # learning rate
        self.gamma = gamma   # discount
        self.env = env
        self.q_table = np.zeros((env.getStateSpaceSize(),
                env.getActionSpaceSize()))



    # deve retornar o id da acao tomada de acordo com uma politica de e-greedy
    # o conjunto de acoes validas para um estado e obtido atraves da funcao sel.enf.getLegalActions
    def getAction(self, state):
        actions = self.env.getLegalActions(state)
        rand =  np.random.random() #gera randomicamente algo entre [0..1] 
       
        if rand < self.epsilon:
            return random.choice(actions)
        else:
            return np.argmax( self.q_table[state, actions] )
        
        "*** SEU CODIGO AQUI ***"


    def update(self, state, action, reward, next_state): #alpha pode ser considerado o learning rate tb da literatura
        "*** SEU CODIGO AQUI ***"
        af = self.env.getLegalActions(next_state)
        amostra = reward + ( self.gamma * np.max(self.q_table[next_state, af]) )
        self.q_table[state, action] = (1 - self.alpha) * self.q_table[state, action] + self.alpha*amostra
        
