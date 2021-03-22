#McGugh example code
# import numpy as np
# from numpy import random
#
#
# def test():
#     # N is batch size ; M different patterns ;
#     # D_in is input dimension ; H is hidden dimension ; D_out is output dimension .
#
#     M = 8
#
#     N, D_in , H, D_out = 100 , 32*M, 128 , M
#
#     x = 0.05* np.random.randn(N, D_in)
#     y = np.zeros((N, D_out))
#
#     foo = 0
#
#     for i in range(N):
#         k = i % M
#         y[i, k] = 1.0
#     for j in range(D_in):
#         if random.rand() > 0.98:
#             x[i, j] = random.rand()
#             foo += 1
#         if j > 32 * k and j < 32 * k + 24:
#             x[i, j] = 1
#
#     xx = x.T
#     yy = y.T
#
#     # Randomly initialize weights
#     w1 = np.random.randn(H, D_in)
#     w2 = np.random.randn(D_out ,H)
#
#     k = 0
#     loss = N*D_out
#     learning_rate = 1e-5
#
#     while (loss > 0.01):
#         # Forward pass : compute predicted y
#         z1 = np.dot(w1, xx)
#         a1 = np.maximum(z1, 0)
#         z2 = np.dot(w2, a1)
#         a2 = z2 # no final activation function
#         # Compute and print loss
#         loss = (np.square(a2 - yy).sum())/N
#         if k %100 == 0:
#             print(k, loss)
#         # Backprop to compute gradients of w1 and w2 with respect to loss
#         err = 2.0 * (a2 - yy)
#         grad_z2 = err  # no final activation function
#         grad_a1 = np.dot(w2.T, grad_z2)
#         grad_z1 = grad_a1.copy()
#         grad_z1[z1 < 0] = 0
#         grad_w2 = np.dot(grad_z2, a1.T)
#         grad_w1 = np.dot(grad_z1, xx.T)
#         # Update weights
#         w1 -= learning_rate * grad_w1
#         w2 -= learning_rate * grad_w2
#         k += 1
#
# test()


#Example of how to use neuron_layer and forward_propagation
import numpy as np
import neuron_layer as n
import forward_propagation as f
def main():
    #make a ANN by making array of NeuronLayer objects
    ann = np.array([])
    for l in range(3):
        tmp = n.NeuronLayer(3, 3)
        ann = np.append(ann, tmp)
    values = np.array([1, 2, 3])
    ann[0].input_value = values
    #checking the updating/overwiting of values when needed
    for t in range(2):
        #put in a 2 dim input input_values
        print("test", t)
        end = f.forward_network(ann)
        for l in range(3):
            print("layer ", l)
            print("input")
            print(ann[l].input_value)
            print("w")
            print(ann[l].w)
            print("z")
            print(ann[l].z)
            print("a")
            print(ann[l].a)

        print("end, ", end)
        values = np.array([2, 4, 6])
        ann[0].input_value = values


if __name__ == '__main__':
    main()