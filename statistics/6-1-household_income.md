[Think Stats Chapter 6 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2007.html#toc60) (household income)

>> Income distribution is skewed to the right as indicated by a  
positive sample skewness, a positive Pearson Median Skewness, and  
a sample mean being greater than the sample median.

Income mean, skewness and fraction of households under the mean increases  
as the upper bound on income increases.  

Pearson median skewness decreases but remains positive as the upper bound  
on income increases. This occurs because this statistic is more robust  
to outliers. Increasing the upper bound on the highest incomes, spreads  
these incomes log linearly over an increasing range making these incomes  
appear as outliers in the sample.  


``` Python

# Solution goes here
print('Mean:', Mean(sample))
print('Median: ', cdf.Value(0.5))
print('Skewness: ', Skewness(sample))
print('Parson Median Skewness: ', PearsonMedianSkewness(sample))
print('Fraction of households with income below mean: ', 
      cdf.Prob(Mean(sample)))

# Upper bound = 10^(5.5)
# Mean: 68116.6656357
# Median:  51226.4544789
# Skewness:  1.6377380521
# Parson Median Skewness:  0.849159334838
# Fraction of households with income below mean:  0.621764196704

# Upper bound = 10^6
# Mean: 74278.7075312
# Median:  51226.4544789
# Skewness:  4.94992024443
# Parson Median Skewness:  0.736125801914
# Fraction of households with income below mean:  0.660005879567

# Upper bound is 10^7
# Mean: 124267.397222
# Median:  51226.4544789
# Skewness:  11.6036902675
# Parson Median Skewness:  0.391564509277
# Fraction of households with income below mean:  0.856563066521


```
