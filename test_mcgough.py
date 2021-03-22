#McGugh example code
import numpy as np
from numpy import random


def test():
    # N is batch size ; M different patterns ;
    # D_in is input dimension ; H is hidden dimension ; D_out is output dimension .

    M = 8

    N, D_in , H, D_out = 100 , 32*M, 128 , M

    x = 0.05* np.random.randn(N, D_in)
    y = np.zeros((N, D_out))

    foo = 0

    for i in range(N):
        k = i % M
        y[i, k] = 1.0
    for j in range(D_in):
        if random.rand() > 0.98:
            x[i, j] = random.rand()
            foo += 1
        if j > 32 * k and j < 32 * k + 24:
            x[i, j] = 1

    xx = x.T
    yy = y.T

    # Randomly initialize weights
    w1 = np.random.randn(H, D_in)
    w2 = np.random.randn(D_out ,H)

    k = 0
    loss = N*D_out
    learning_rate = 1e-5

    while (loss > 0.01):
        # Forward pass : compute predicted y
        z1 = np.dot(w1, xx)
        a1 = np.maximum(z1, 0)
        z2 = np.dot(w2, a1)
        a2 = z2 # no final activation function
        # Compute and print loss
        loss = (np.square(a2 - yy).sum())/N
        if k %100 == 0:
            print(k, loss)
        # Backprop to compute gradients of w1 and w2 with respect to loss
        err = 2.0 * (a2 - yy)
        grad_z2 = err  # no final activation function
        grad_a1 = np.dot(w2.T, grad_z2)
        grad_z1 = grad_a1.copy()
        grad_z1[z1 < 0] = 0
        grad_w2 = np.dot(grad_z2, a1.T)
        grad_w1 = np.dot(grad_z1, xx.T)
        # Update weights
        w1 -= learning_rate * grad_w1
        w2 -= learning_rate * grad_w2
        k += 1

test()
