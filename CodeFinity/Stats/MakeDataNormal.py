#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:43:00 2022

@author: craigrupp
"""

# Confidence Interval Refresh
# =============================================================================
# The confidence interval is the measure of certainty for the defined rate of confidence for the specific value. 
# 
# For instance, if we have data on the phone's price, we can say that the phone will cost between 1 and 1.5 thousand dollars with a confidence of 95%.
# 
# 95% of all the data would be between range (1,000 - 1,500) with the upper and lower bound splitting the remaining 5% of the data spread
# 
# With the confidence level of 95% we can state that the mean value lies between the lower and the upper bound. 
# We can choose any rate for the interval, but the most commonly used is 95%, and another less popular variant is 99%.
# =============================================================================
# Import pandas library
import pandas as pd
# Import matplotlib.pyplot library
import matplotlib.pyplot as plt
# Import seaborn library
import seaborn as sns
# Import scipy.stats library
import scipy.stats as st
# Import numpy library
import numpy as np

# Read csv file
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/confidence.csv', index_col = 0)

# Output the first five observations
print(data.head())

# Let's look at the value_counts for the body_mass
print(data['body_mass_g'].value_counts())

# Create the histplot
plot = sns.histplot(data = data,
                  x = 'body_mass_g',
                  kde = True)
plot.set_title('Penguins')
plot.set(xlabel = 'The Mass', ylabel = 'The Quantity')
plt.show()


# Bootstrapping - We create many simulated samples by resampling a single dataset.
# =============================================================================
# To find the confidence interval, the data set should be normal. 
# As you may recall from the Probability Theory course, confidence interval definition stems from the normal distribution.
# =============================================================================
# =============================================================================
# But we can not consider that each distribution is normal; it is always better to bring it to the normal form. 
# According to the central limit theorem (you will learn it in the following chapters), 
# we can assume that the distribution of sample means can be approximated to normal, and the size of its distribution is larger.
# =============================================================================
# Random Object
import random
# Import norm object
from scipy.stats import norm
np.random.seed(0)

# Create random distribution, loc = mean, size = distribution size - Return is a numpy.ndarray (transform to list for .sample method)
list_data = norm.rvs(loc = 200, size = 10000)
print(list_data[0:5], type(list_data))

mean_list = []
# Define the for loop
for i in range(50):
    # Create random samples
    item = random.sample(list(list_data), 4)
    # Find the mean value of the sample
    mean = np.mean(item)
    # Append the mean value to the mean_list
    mean_list.append(mean)

print(np.mean(list_data))
print(np.mean(mean_list))




# Apply Bootstrap to penguin's weight columns :
print(data.isna().sum())
# Good practice here but not required as dataframe has no null values in any of its' columns
data.dropna(inplace = True)
# No Change
print(data.isna().sum())
list_data = data['body_mass_g'] # Series return can be changed to a list
# print(list_data[0:5], list_data[0:5].values) # sane return here as the list type conversion of the series below
print(type(list_data.values)) # <class 'numpy.ndarray'> (Not a sequence for the sample method)
# hey = list(list_data)
# print(hey[0:5])

mean_list = []
# Define the for loop
for i in range(2000):
    # Create random samples
    item = random.sample(list(list_data), 10)
    # Find the mean value of the sample
    mean = np.mean(item)
    # Append the mean value to the mean_list
    mean_list.append(mean)

print(np.mean(list_data))
print(np.mean(mean_list))



# New Data Set
# Read csv file
data_mass = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/mean_mass.csv')
# Extract column 'mass'
mean_list_mass = data_mass['mass']

# Create the histplot
plot = sns.histplot(mean_list, kde=True)
plot.set_title('Penguins')
plot.set(xlabel = 'The Mean of the Mass', ylabel = 'The Quantity')
# Output the histplot
plt.show()




## Calculating Confidence Interval
# =============================================================================
# Here we should define the average weight of a penguin with the confidence of 95%.
# So in our case, we drop 2.5% of data from the left side and the same with the right side. Other data corresponds to 95% of all data.
# =============================================================================
# Creating random normal distribution
dist = norm.rvs(size = 1000, loc = 50, scale = 2)
print(type(dist), len(dist))
# Finding confidence interval - with numpy percentile method on numpy.ndarray with percentiles as 100% based on distribution
confidence = np.percentile(dist, [2.5, 97.5])
# Let's peek at the median
median = np.percentile(dist, 50)
print(median)

# Creating the histplot
plot = sns.histplot(data = dist, kde = True)
plot.set_title('Random Values')
plot.set(xlabel = 'X', ylabel = 'Y')
plt.show()

print(confidence)
print(st.norm.interval(alpha=0.95, loc=np.mean(dist), scale=np.std(dist, ddof=1)))

# Task
# =============================================================================
# Your task here is to apply the percentile method to find the interval for the mean 
# value of the penguins' size with the confidence of 95% & 99%.

## Confidence Interval - find tails on distribution
# =============================================================================
peng_95 = data_mass['mass']
# Find confidence interval for 95% - Find the tails and outer intervals
confidence_95 = np.percentile(peng_95, [2.5, 97.5])

# Create the histplot
plot = sns.histplot(data = peng_95, kde=True)
plot.set_title('Penguins')
plot.set(xlabel = 'The Mean of the Mass', ylabel = 'The Quantity')
# Output the histplot
plt.show()

# Output the confidence interval
print(confidence_95) # [3737.5 4715. ]


## 99th confidence interval = 0.5 - 99.5 of distribution
peng_99 = data_mass['mass']
confidence_99 = np.percentile(peng_99, [0.5, 99.5])

ninenine_plot = sns.histplot(data = peng_99, kde=True)
ninenine_plot.set_title('Penguins')
ninenine_plot.set(xlabel = 'The Mean of the Mass', ylabel = 'The Quantity')
# Output the histplot
plt.show()

print(confidence_99) # [3607.4625 4870.125 ]

# Notice how the confidence tails extend to further of the distribution to include 99% of the data 
## 99% confident any penguin mass would live in this range between the intervals




## Python - Calculate Confidence Interval - !!  Applied only to Normal Distribution 
# =============================================================================
# Obviously, Python has a function that can calculate a confidence interval for us. 
# But I want to remind you that first, we turned our distribution to normal; otherwise, your measurements will be spoiled by enormous values. 
# So the following method can be applied only to normal distribution.
# =============================================================================
# =============================================================================
# scipy.stats as st module usage for python calculation
# st.norm.interval - method for findind confidence intervals
# st.sem - value of the standard error of the mean 
#  (Standard error is calculated by dividing the standard deviation of the sample by the square root of the sample size)

# st.norm.interval(alpha=0.95, loc=np.mean(dist), scale=st.sem(dist))
# 
# alpha : parameter corresponds to the level of confidence,
# loc : parameter corresponds to the mean value of the distribution, counted manually,
# scale : corresponds to the value of standard error of the mean, counted manually. (Looks like standard deviation works as well)
# =============================================================================
# Your task now is to calculate the confidence interval to define the mean of penguins' size using scipy.stats library (95% confidence interval of mean)

data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a849660e-ddfa-4033-80a6-94a1b7772e23/section_1/mean_mass.csv')
mean_list = data['mass']
# Find the confidence interval
confidence = st.norm.interval(alpha = .95,
                          loc = np.mean(mean_list),
                          scale = st.sem(mean_list))

# Create the histplot (use penguins column)
plot = sns.histplot(mean_list, kde=True)
# Set the title 
plot.set_title('Penguins')
# Set labels for axis
plot.set(xlabel = 'The Mean of the Mass',
           ylabel ='The Quantity')
# Output the histplot
plt.show()

# Output the confidence interval
print(confidence) # calculating the 95% confidence interval of the mean (see how scale is used )
# (4188.431356119257, 4210.566143880743)

## Check Manually like above calculation for 95% of total distribution
print(np.percentile(list(mean_list), [2.5, 97.5])) # [3737.5, 4715.0 ]
## Use Scipy.stats (aliased as st) ! Pretty close to our manual calculation - This would be the confidence level of the full distribution I believe
print(st.norm.interval(alpha=0.95, loc=np.mean(mean_list), scale=np.std(mean_list, ddof=1))) # (3704.54984, 4694.44765)


# Confidence of 99%, is It Accurate? - (Confidence Interavl of Mean)
# =============================================================================
# Let's compare the interval for the mean size of the penguin with the level of confidence of 95% and 99%. 
# For the first one, we had such results: (4193.492547812758, 4215.899952187242).
# 
# Would imagine this stretches out our levels a bit
# =============================================================================

# Find the confidence interval (Calculating Standard error of the mean per the detailing above)
confidence = st.norm.interval(alpha = .99,
                  loc = np.mean(mean_list),
                  scale = np.std(mean_list) / np.sqrt(len(mean_list)))

print(confidence)
# print(confidence) : (4184.957365629527, 4214.0401343704725)

# Using the equation for the standard error of the mean (see scale arg above) : close to the stats module output .. not bad


confidence_mod = st.norm.interval(alpha = .99,
                  loc = mean_list.mean(),
                  scale = st.sem(mean_list))

print(confidence_mod)
#print(confidence_mod) : (4184.953728919611, 4214.043771080388)



## Deal with Small Distribution
# =============================================================================
# The data is not always perfect; it usually requires preprocessing or other manipulations. 
# Sometimes we deal with a small sample size of less than 30.
# 
# 
# In such cases, we work with the Student's t-distribution; it is almost the same as a normal one but has fewer observations, usually less than 30.
# It can be a part of a huge population; therefore, if we have data about the sample, not about the population, 
# we do not know the standard deviation of the population (it is a sign to use Student's T distribution). 
# It means that values are distributed normally, but look at the graph; it has heavier tails due to the size 
# (the distribution of heights of first-graders in centimeters in one class):
# =============================================================================
# Ex 
data = [104, 106, 106, 107, 107, 107, 108, 108, 108, 108, 108, 109, 109, 109, 110, 110, 111, 111, 112]
# Creating the histplot
plot = sns.histplot(data = data, kde = True, bins = 7)
plot.set_title("Student's Heights")
plot.set(xlabel = 'The Height', ylabel = 'The Quantity')
plt.show()

# =============================================================================
# Here, we deal with the population sample; the amount of observation is 19. 
# Let's assume that we already know that the population of first-graders distributed normally. 
# We want to know the interval for the mean height value with the standard 95% of confidence.
# 
# We should figure out the term degrees of freedom to do it.

# When we want to find the mean value, the degrees of freedom equal the sample size - 1 
# (in this course, the formula for finding degrees of freedom always will be sample size - 1). 
# Indeed, it defines the number of independent variables of the vector that is sufficient to find out the characteristics of the vector.
# =============================================================================
# =============================================================================
# How to calculate confidence interval?
# 
# st.t.interval(alpha = 0.95, df = len(data)-1, loc = data.mean(), scale = st.sem(data))
# 
# From scipy.stats we should use the t.interval function for the Student's T distribution.
# As it was before, alpha means the confidence level.
# df corresponds to the degrees of freedom, counted manually.
# loc defines the mean, counted manually.
# sem means the standard error of the sample, counted manually.
# =============================================================================
# st.t.interval with degrees of freedom (len of data/sequence - 1) (looking for 95% interval for mean)
confidence = st.t.interval(alpha = .95,
                             df = len(data) - 1,
                             loc = np.mean(data),
                             scale = st.sem(data))

print(confidence)
print(sum(data), len(data))




## Task
# =============================================================================
# Here in the Task Code, you have the sample of the kitten's height. 
# This data describes the only sample and can not allow us to receive information about the whole population; it is the right time for Student's T distribution. 
# Find the interval that includes the mean value of the mean size of the cat in centimeters
# =============================================================================

data = [17, 18, 19, 19, 20, 20, 20, 21, 21, 21, 21, 22, 22, 22, 22, 23, 23, 23, 23, 23, 24, 24, 24, 25, 25, 26, 26, 27, 28]
# Calculate the confidence interval
confidence = _ _ _(alpha = _ _ _,
                  df = _ _ _,
                  _ _ _,
                  _ _ _)

# Create the histplot
plot = _ _ _.histplot(_ _ _)
# Set the title
_ _ _(_ _ _)
plot.set(xlabel = 'The Size', ylabel = 'The Quantity')
# Output the histplot
plt._ _ _()

# Output the interval
print(_ _ _)
















