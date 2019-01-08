#!/usr/bin/python
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import sys

'''
frame perplexity:

means:

0: 271466.8599850139
1: 6909661.758299611
2: 8019045.9765143525
3: 8209030.542357509
4: 15552.55992031817
5: 82355.51572574466
6: 203653.49746745112


cis:

0: 268344.544297, 275208.914068
1: 6931442.71671, 7003668.47118
2: 8034355.02656, 8138045.67082
3: 8224872.25322, 8334569.62013
4: 15437.4794204, 15665.4216152
5: 81465.960972, 83263.8052139
6: 202094.545367, 205328.018364

'''
   
perp_cis = [[268344.544297, 275208.914068],[6931442.71671, 7003668.47118],[8034355.02656, 8138045.67082],
			[8224872.25322, 8334569.62013],[15437.4794204, 15665.4216152],[81465.960972, 83263.8052139],[202094.545367, 205328.018364]]
perp_means = [271466.8599850139, 6909661.758299611, 8019045.9765143525, 8209030.542357509, 15552.55992031817,
				82355.51572574466, 203653.49746745112]
				
def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    with open(filename, 'rb') as input:
        obj = pickle.load(input)
    return obj


#CIS = load_object("ci_info.pkl")

title_list = ["2 yo, adult-child", "2 yo, child-child", "3 yo, adult-child", "3 yo, child-child", "4 yo, adult-child", "4 yo, child-child", "adult-adult"]
count = 0

x = []
y_bottom = []
y_top = []
for c, value in enumerate(perp_cis,1):
	x.append(c)
	y_bottom.append(value[0])
	y_top.append(value[1])
#x = [1,2,3,4,5,6,7]#["freq of input", "lexical class" ,"subjectivity"]
#y_bottom = [float(freq_ci[0]),float(lex_ci[0]), float(sub_ci[0])]
#y_top = [float(freq_ci[1]),float(lex_ci[1]), float(sub_ci[1])]
x_left = [thing-.1 for thing in x]#[x[0]-.1, x[1]-.1, x[2]-.1]
x_right = [thing +.1 for thing in x]#[x[0]+.1, x[1]+.1, x[2]+.1]
#
#means = CIS[file][3]#[-379.424232553,-407.26802576,-361.796573284]
#means_series = pd.Series.from_array(means)
#objects = ('freq', 'lex', 'sub')
plt.figure()
plt.bar(x, perp_means)
#plt.figure(figsize=(12, 8))
#ax = means_series.plot(kind='bar')
plt.style.use('ggplot')
plt.hlines(y_bottom, x_left, x_right)
plt.hlines(y_top, x_left, x_right)
plt.vlines(x, y_bottom, y_top)
#plt.xticks(x, objects)
plt.title('frame perplexity per instantiation')
plt.xlabel('framing thing')
plt.ylabel('av perplexity')
for thing in x:
	plt.text(thing-.18,perp_means[thing-1]*.75, str(round(perp_means[thing-1])), color = 'purple', size = 12)
plt.savefig('perplexity.png')


#adult-adult 

