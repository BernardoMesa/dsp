# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:39:26 2017

@author: BernardoMesa
"""

import sys
import os

# Complete the function below.

def sort_last(tuples):
    tuples = list(tuples) 
    return map(eval,tuples.sort(key=lambda pair: pair[1]))


tuples = sys.stdin.read().split('\n')
tuples = map(eval,tuples)
res = sort_last(tuples)
for t in res:
    print(t)