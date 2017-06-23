[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>>

``` Python

thinkplot.PrePlot(2, rows=2)


v=0
lam = 2
Ls = []
n = 10
for i in range(0,1000):
    sample = np.random.exponential(1.0/lam,n)
    L = 1/sample.mean()
    Ls.append(L)

    
cdf = thinkstats2.Cdf(Ls)
CI = cdf.Percentile(5), cdf.Percentile(95)
thinkplot.Cdf(cdf)
thinkplot.Plot( [CI[0],CI[0]] , [0,1],color='0.8', linewidth=3)
thinkplot.Plot( [CI[1],CI[1]] , [0,1],color='0.8', linewidth=3)
thinkplot.Show(xlabel='Estimate',ylabel='CDF',axis=[0,5,0,1])



stderr = np.sqrt(np.mean([(estimate - lam)**2 for estimate in Ls]))
print('stderr: ',stderr)

print('CI:', CI)


# Plot stderr against several values of n
thinkplot.SubPlot(2)
StdErrs=[]

for n in range(10,110,10):
    Ls = []
    for i in range(1000):
        sample = np.random.exponential(1.0/lam,n)
        L = 1/sample.mean()
        Ls.append(L)
    
    stderr = np.sqrt(np.mean([(estimate - lam)**2 for estimate in Ls]))
    StdErrs.append(stderr)
        

thinkplot.Plot(range(10,110,10),StdErrs)
thinkplot.Show(xlabel='sample size',ylabel='stderr',title='Lambda Estimate')

'''
