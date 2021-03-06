import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)

    Inputs have dimension D, there are C classes, and we operate on minibatches
    of N examples.

    Inputs:
    - W: A numpy array of shape (D, C) containing weights.
    - X: A numpy array of shape (N, D) containing a minibatch of data.
    - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
    - reg: (float) regularization strength

    Returns a tuple of:
    - loss as single float
    - gradient with respect to weights W; an array of same shape as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train = X.shape[0]
    for i in range(num_train):
        y_pred = X[i, :].dot(W)
        loss = loss - y_pred[y[i]] + np.log(np.sum(np.exp(y_pred)))
        
        dW[:, y[i]] -= X[i, :].T
        dW += np.exp(y_pred) * X[i, :].reshape(-1, 1) / np.sum(np.exp(y_pred))
            
    loss /= num_train
    loss += reg * np.sum(W * W)
    
    dW /= num_train
    dW += 2 * reg * W

    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train = X.shape[0]
    
    y_pred = X.dot(W)
    correct_score = y_pred[range(num_train), y]
    
    loss -= np.sum(correct_score)
    loss += np.sum(np.log(np.sum(np.exp(y_pred), axis=1)))
    
    dW -= (X.T).dot(np.eye(np.max(y) + 1)[y])    # ?????????onehot
    dW += (X.T).dot(np.exp(y_pred) / np.sum(np.exp(y_pred), axis=1).reshape(-1, 1))
     
    loss /= num_train
    loss += reg * np.sum(W * W)

    dW /= num_train
    dW += 2 * reg * W

    #############################################################################
    #                          END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW

