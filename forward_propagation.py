import numpy as np


class FeedForwardNetwork_Vectorised:

    def __init__(self, d_in, d_hidden, d_out):
        np.random.seed(0)
        self.W1 = np.random.randn(d_hidden, d_in)
        self.W2 = np.random.randn(d_out, d_hidden)

    def ReLU(self, X):
        return np.maximum(X, 0)

    def forward_pass(self, X):
        self.A1 = np.matmul(X, self.W1)
        self.H1 = self.ReLU(self.A1)
        self.A2 = np.matmul(self.H1, self.W2)
        self.H2 = self.ReLU(self.A2)
        return self.H2