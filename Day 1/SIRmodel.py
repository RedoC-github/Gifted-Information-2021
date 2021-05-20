class SIR:
    def __init__(self, S, I, R, beta, gamma):
        self.N = S + I + R
        self.S = S
        self.I = I
        self.R = R
        self.beta = beta
        self.gamma = gamma
    
    def update(self):
        self.S -= self.beta * self.S * self.I / self.N
        self.I += self.beta * self.S * self.I / self.N - self.gamma * self.I
        self.R += self.gamma * self.I

