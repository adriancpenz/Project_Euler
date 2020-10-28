"""
Project Euler 001
"""

import math as m
import time


"""
Optimized Algorithm
"""

def SmartSum(N,a,b):
    
    start = time.time()
    
    div_a = m.floor(N/a)
    div_b = m.floor(N/b)
    div_ab = m.floor(N/a/b)
    
    sum_a = a * div_a * (div_a+1)/2
    sum_b = b * div_b * (div_b+1)/2
    
    sum_ab = a*b * div_ab * (div_ab+1)/2
    
    end = time.time()
    
    return [sum_a + sum_b - sum_ab,end-start]
    

"""
Basic Algorithm
"""

def MultiSum(N,a,b):
    start = time.time()
    total = 0
    
    for i in range(1,N+1):
        if i % a == 0 or i % b == 0:
            total += i
            print(i)
            
    end = time.time()
    return [total,end-start]