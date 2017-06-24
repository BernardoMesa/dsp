[Think Stats Chapter 8 Exercise 3](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77)

---

>> This way of making an estimate is not biased since the MSE  
tends to zero as the number of experiments increases.  
The standard error seems to converge to the square root of  
lambda.  
As lambda increases the standard error tends to increase.

``` Python

def SimulateGame(lam):
    goals = 0
    total_time = 0
    
    while total_time < 1:
        time = np.random.exponential(1.0/lam,1)
        total_time += time
        if total_time <1:
            goals += 1
    
    return goals

def SimulateManyGames(lam,n=1000):
    goals = []
    
    for i in range(n):
        goals.append(SimulateGame(lam))
    

    cdf = thinkstats2.Cdf(goals)
    thinkplot.Cdf(cdf)
    CI = cdf.Percentile(5),cdf.Percentile(95)
    thinkplot.Plot( [CI[0],CI[0]] , [0,1],color='0.8', linewidth=3)
    thinkplot.Plot( [CI[1],CI[1]] , [0,1],color='0.8', linewidth=3)
    thinkplot.Show(xlabel='Estimate',ylabel='CDF')

    merr = MeanError(goals,lam)
    stderr = RMSE(goals,lam)
    print('Mean Error: ', merr)
    print('RMSE: ', stderr)
    
    print('CI: ', CI)
    print('CI Range: ', CI[1]-CI[0])

SimulateManyGames(2,10000)

```

---
