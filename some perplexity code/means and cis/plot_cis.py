#!/usr/bin/python
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import sys

'''
infile = open('2-adult-child-10000.txt', 'r')
infile1 = open('2-adult-child-mean.txt', 'r')
infile2 = open('2-child-child-10000.txt', 'r')
infile3 = open('2-child-child-mean.txt', 'r')
infile4 = open('3-adult-child-10000.txt', 'r')
infile5 = open('3-adult-child-mean.txt', 'r')
infile6 = open('3-child-child-10000.txt', 'r')
infile7 = open('3-child-child-mean.txt', 'r')
infile8 = open('4-adult-child-10000.txt', 'r')
infile9 = open('4-adult-child-mean.txt', 'r')
infile10 = open('4-child-child-10000.txt', 'r')
infile11 = open('4-child-child-mean.txt', 'r')
infile12 = open('adult-adult-10000.txt', 'r')
'''
    
#mean_list = [readinfile1, readinfile3, readinfile5, readinfile7, readinfile9, readinfile11]

#file_list = [readinfile, readinfile2, readinfile4, readinfile6, readinfile8, readinfile10, readinfile12]

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    with open(filename, 'rb') as input:
        obj = pickle.load(input)
    return obj


CIS = load_object("ci_info.pkl")
print CIS
title_list = ["2 yo, adult-child", "2 yo, child-child", "3 yo, adult-child", "3 yo, child-child", "4 yo, adult-child", "4 yo, child-child", "adult-adult"]
count = 0
for file in CIS.keys():
	#
	freq_ci = CIS[file][0]
	lex_ci = CIS[file][1]
	sub_ci = CIS[file][2]
	x = [1,2,3]#["freq of input", "lexical class" ,"subjectivity"]
	y_bottom = [float(freq_ci[0]),float(lex_ci[0]), float(sub_ci[0])]
	y_top = [float(freq_ci[1]),float(lex_ci[1]), float(sub_ci[1])]
	x_left = [x[0]-.1, x[1]-.1, x[2]-.1]
	x_right = [x[0]+.1, x[1]+.1, x[2]+.1]
	#
	means = CIS[file][3]#[-379.424232553,-407.26802576,-361.796573284]
	#means_series = pd.Series.from_array(means)
	objects = ('freq', 'lex', 'sub')
	plt.figure()
	plt.bar(x, means)
	#plt.figure(figsize=(12, 8))
	#ax = means_series.plot(kind='bar')
	plt.style.use('ggplot')
	plt.hlines(y_bottom, x_left, x_right)
	plt.hlines(y_top, x_left, x_right)
	plt.vlines(x, y_bottom, y_top)
	plt.xticks(x, objects)
	plt.title(title_list[count])
	plt.xlabel('representation')
	plt.ylabel('log likelihood of representation')
	for thing in x:
		plt.text(thing-.18,means[thing-1]*.75, str(round(means[thing-1])), color = 'purple', size = 12)
	plt.savefig(title_list[count]+'.png')
	count +=1

#adult-adult 

