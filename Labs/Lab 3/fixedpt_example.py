"""
 This script explores the use of the fixed point method.  
 Two functions are considered that have different properties.
 I like to use this code before I talk about convergence analysis
 for the fixed point method as motivation.
"""

############################################# 
"""
Copyright (C) 2025  Adrianna M. Gillman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
############################################# 



# import libraries
import numpy as np
    
def driver():

# test functions 
#     f1 = lambda x: 1+0.5*np.sin(x)
# fixed point is alpha1 = 1.4987....
     f1 = lambda x: (10 / (x+4))**0.5
#fixed point is alpha1 = 1.3652300134140976

     f2 = lambda x: 3+2*np.sin(x)
#fixed point is alpha2 = 3.09... 

     Nmax = 100
     tol = 1e-6
     p01 = np.zeros((100,1))
     p02 = np.zeros((100,1))
# test f1 '''
     x0 = 1.5
     [xstar, ier, p1, count] = fixedpt(f1,x0,tol,Nmax,p01)
     [alpha, lam] = convapprox(p1, count, xstar)
     print('the approximate fixed point is:',xstar)
     print('f1(xstar):',f1(xstar))
     print('Error message reads:',ier)
     print('Alpha is',alpha)
     print(lam)
    
#test f2 '''
     x0 = 0.0
     [xstar,  ier, p2, count] = fixedpt(f2,x0,tol,Nmax,p02)
     [alpha, lam] = convapprox(p2, count, xstar)
     print('the approximate fixed point is:',xstar)
     print('f2(xstar):',f2(xstar))
     print('Error message reads:',ier)
     print('Alpha is',alpha)
     print(lam)



# define routines
def fixedpt(f,x0,tol,Nmax,p):

    ''' x0 = initial guess''' 
    ''' Nmax = max number of iterations'''
    ''' tol = stopping tolerance'''

    count = 0
    while (count <Nmax):
       p[count,0] = f(x0)
       count = count +1
       x1 = f(x0)
       if (abs(x1-x0) <tol):
          xstar = x1
          ier = 0
          return [xstar,ier, p, count]
       x0 = x1

    xstar = x1
    ier = 1
    return [xstar, ier, p, count]

def convapprox(p, count, xstar):
    lam = np.abs(p[count, 0] - xstar) / np.abs(p[count - 1, 0] - xstar)
    alpha = np.log(np.abs(p[count,0] / xstar)) / np.log(np.abs(xstar / p[count - 1,0]))
    return [alpha, lam]
    

driver()
