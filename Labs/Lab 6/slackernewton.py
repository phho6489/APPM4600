import numpy as np
import math
import time
from numpy.linalg import inv 
from numpy.linalg import norm 

def driver():

    # x0 = np.array([0.1, 0.1, -0.1])
    x0 = np.array([0.1, 0])
        
    Nmax = 100
    tol = 1e-10

    t = time.time()
    for j in range(50):
      [xstar,ier,its] =  Newton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Newton: the error message reads:',ier) 
    print('Newton: took this many seconds:',elapsed/50)
    print('Netwon: number of iterations is:',its)    

    t = time.time()
    for j in range(20):
      [xstar,ier,its] =  LazyNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Lazy Newton: the error message reads:',ier)
    print('Lazy Newton: took this many seconds:',elapsed/20)
    print('Lazy Newton: number of iterations is:',its)

    t = time.time()
    for j in range(20):
       [xstar,ier,its] = SlackerNewton(x0,tol,Nmax)
    elapsed = time.time()-t
    print(xstar)
    print('Slacker Newton: the error message reads:',ier)
    print('Slacker Newton: took this many seconds:',elapsed/20)
    print('Slacker Newton: number of iterations is:',its)

def evalF(x): 
# vector function that you want to find the roots of

    F = np.zeros(2)
    
    # F[0] = 4*x[0]**2 + x[1]**2 - 4
    # F[1] = x[0] + x[1] - np.sin(x[0] - x[1])

    F[0] = np.exp(10*x[0]) + x[1] - 1
    F[1] = 10*x[0]**2 + x[1]
 
    return F

def evalJ(x): 
# Jacobian of the vector function you want to find the roots of
    
    # J = np.array([[8*x[0], 2*x[1]],
    #              [1 - np.cos(x[0]-x[1]), 1 + np.cos(x[0]-x[1])]])

    J = np.array([[10*np.exp(10*x[0]), 1],
                  [20*x[0], 1]])

    return J

def Newton(x0,tol,Nmax):

    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    for its in range(Nmax):
       J = evalJ(x0)
       Jinv = inv(J)
       F = evalF(x0)
       
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier, its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]

def LazyNewton(x0,tol,Nmax):

    ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
    ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
    ''' Outputs: xstar= approx root, ier = error message, its = num its'''

    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):

       F = evalF(x0)
       x1 = x0 - Jinv.dot(F)
       
       if (norm(x1-x0) < tol):
           xstar = x1
           ier =0
           return[xstar, ier,its]
           
       x0 = x1
    
    xstar = x1
    ier = 1
    return[xstar,ier,its]   

def SlackerNewton(x0,tol,Nmax):
    J = evalJ(x0)
    Jinv = inv(J)
    for its in range(Nmax):
        F = evalF(x0)
        x1 = x0 - Jinv.dot(F)

        if (its % 2):
           J = evalJ(x1)
           Jinv = inv(J)

        if (norm(x1-x0) < tol):
           xstar = x1
           ier = 0
           return[xstar,ier,its]

        x0 = x1
    xstar = x1
    ier = 1
    return[xstar,ier,its]

if __name__ == '__main__':
    # run the drivers only if this is called from the command line
    driver()   