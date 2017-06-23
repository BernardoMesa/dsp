[Think Stats Chapter 7 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2008.html#toc70) (weight vs. age)

>> The variables seem to be uncorrelated with a pearson and spearman correlation coefficients of 0.07 and 0.09 respectively.
Baby weights distribution seems to slightly shift higher as mothers age increases from the teens to the mid-twenties, but seems to stay relatively stable after that.

``` Python

import first
import thinkstats2
import thinkplot

live, firsts, others = first.MakeFrames()
live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

bins = np.arange(5,50,5)
indices = np.digitize(live.agepreg,bins)
groups = live.groupby(indices)

# Exclude edges with few samples
meanAge = [group.agepreg.mean() for i, group in groups][1:-1]
cdfs = [ thinkstats2.Cdf(group.totalwgt_lb, label = 'i') for i, group in groups][1:-1]


for pc in [25,50,75]:
    wgtPerc = [cdf.Percentile(pc) for cdf in cdfs]
    thinkplot.Plot(meanAge,wgtPerc, label=pc)

thinkplot.Show(xlabel = 'age',ylabel='weight',legend = True)

# Scatter plot

thinkplot.Scatter(live.agepreg,live.totalwgt_lb,alpha=0.1,s=10)

# Correlations
corr_pearson = live.agepreg.corr(live.totalwgt_lb)
corr_spearman = live.agepreg.corr(live.totalwgt_lb,method='spearman')
corr_pearson, corr_spearman

```
