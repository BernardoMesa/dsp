[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> REPLACE THIS TEXT WITH YOUR RESPONSE


Firsts mean:  7.204107733975324
Others mean:  7.301399825021872
Cohen's d:  -0.0691182534882
The effect size is small

Effect size |d | Reference
------      ---  ------ 
Very small |0.01 | Sawilowsky, 2009
Small |0.20 |Cohen, 1988
Medium |0.50 |Cohen, 1988
Large |0.80 |Cohen, 1988
Very large |1.20 |Sawilowsky, 2009
Huge |2.0 |Sawilowsky, 2009

import numpy as np
import nsfg
import first


def ces(x_group,y_group):
    mean_x = x_group.mean()
    mean_y = y_group.mean()
    
    size_x = len(x_group)
    size_y = len(y_group)
    
    var_x = x_group.var()
    var_y = y_group.var()
    
    s = np.sqrt((size_x*var_x + size_y*var_y)/(size_x+size_y))
    
    return (mean_x-mean_y)/s
    
    
preg = nsfg.ReadFemPreg()

firsts = preg[preg.pregordr==1]
others = preg[preg.pregordr!=1]


print('Firsts mean: ', firsts.totalwgt_lb.mean())
print('Others mean: ', others.totalwgt_lb.mean())

cohen_d = ces(firsts.totalwgt_lb,others.totalwgt_lb)

