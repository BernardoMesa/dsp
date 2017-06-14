[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> REPLACE THIS TEXT WITH YOUR RESPONSE

Since each element in the random vector is unique, the pdf of the distribution has height 1/1000 (1000 elements in vector) indicating the probability of picking that element from the vector is 1 in 1000. The pmf should have height 1 from [0,1]

``` python
num = np.random.random(1000)

thinkplot.PrePlot(2,cols=2)
pmf = thinkstats2.Pmf(num)
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number', ylabel='Pmf')

thinkplot.SubPlot(2)
cdf = thinkstats2.Cdf(num)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Number', ylabel='Cdf')
```
