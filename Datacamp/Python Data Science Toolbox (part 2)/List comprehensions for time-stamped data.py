# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:04:24 2019

@author: Zac_Fang
"""
# Extract the created_at column from df: tweet_time
import pandas as pd
import time
df = pd.read_csv("") # not executable cuz not such file in local computer
tweet_time = df['created_at']
# Extract the clock time: tweet_clock_time
#3th beginning = [2:] inclusive 
#19th end = [:19th] exclusive
tweet_clock_time = [entry[11:19] for entry in tweet_time]
# Print the extracted times
print(tweet_clock_time)
for i in tweet_clock_time:
    print(i)
