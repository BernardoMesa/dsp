[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> REPLACE THIS TEXT WITH YOUR RESPONSE

#Number of kids in a household


Unbiased:  1.02420515504  

Biased:  2.40367910066  

```python

resp = nsfg.ReadFemResp()
numkdhh = resp.numkdhh

pmf = thinkstats2.Pmf(numkdhh, label='actual')
biased_pmf = BiasPmf(pmf, label='observed')

thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='num_kids', ylabel='PMF') 
print('Unbiased: ', pmf.Mean())
print('Biased: ',biased_pmf.Mean())


```