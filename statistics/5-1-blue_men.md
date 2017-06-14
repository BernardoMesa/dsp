[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> REPLACE THIS TEXT WITH YOUR RESPONSE

34% of the population is between 5'10 and 6'1 tall.  

``` python
import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu,scale=sigma)


def intocm(feet,inches):
    tot_inches = feet*12+inches
    return tot_inches*2.54

x_min = intocm(5,10)
x_max = intocm(6,1)
x_min, x_max

ppl = dist.cdf(x_max)-dist.cdf(x_min)
print("% population between 5'10 and 6'1 height: ", ppl)

```