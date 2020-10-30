"""
Project Euler 002
"""

import math as m
import time


 


"""
Optimized Calculation
"""
def Opt_fib(n):
    start = time.time()
    phi = ( 1 + 5**0.5)/ 2
    psi = (1 - 5**0.5)/2
    n_max = m.log(n*5**0.5) / m.log(phi)
    
    m_max = m.floor(n_max/3)
    
    sum_phi = (phi ** (3*(m_max+1)) - 1) / (phi ** 3 -1) / 5**0.5
    sum_psi = 1 / (1- psi ** 3) / 5**0.5
    
    end = time.time()
    
    return [round(sum_phi - sum_psi),end-start]






"""
Basic Algorithm
"""

def Base_fib(n):
    start = time.time()
    
    i = 1
    j = 2
    
    total = 0
    
    while j < n:
        
        if j%2 == 0:
            total += j
            
        j2 = j
        j = j + i
        i = j2
        print([i,j])
        
    end = time.time()
    
    return [total, end-start]