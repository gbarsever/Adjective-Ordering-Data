#!/usr/bin/python
from __future__ import division
import pickle
import matplotlib.pyplot as plt
import numpy as np

def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename):
    with open(filename, 'rb') as input:
        obj = pickle.load(input)
    return obj

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


readinfile = infile.readlines()
readinfile1 = infile1.readlines()
readinfile2 = infile2.readlines()
readinfile3 = infile3.readlines()
readinfile4 = infile4.readlines()
readinfile5 = infile5.readlines()
readinfile6 = infile6.readlines()
readinfile7 = infile7.readlines()
readinfile8 = infile8.readlines()
readinfile9 = infile9.readlines()
readinfile10 = infile10.readlines()
readinfile11 = infile11.readlines()
readinfile12 = infile12.readlines()

file_list = [readinfile, readinfile2, readinfile4, readinfile6, readinfile8, readinfile10, readinfile12]

mean_list = [readinfile1, readinfile3, readinfile5, readinfile7, readinfile9, readinfile11]

freq_adult = []
lex_adult = []
sub_adult = []

for g in readinfile12:
	if g[0] == '-':
		x = g.rstrip()
		y = x.split('\t')
		freq_adult.append(float(y[0]))
		lex_adult.append(float(y[1]))
		sub_adult.append(float(y[2]))
freq_mean = np.mean(np.array(freq_adult))
lex_mean = np.mean(np.array(lex_adult))
sub_mean = np.mean(np.array(sub_adult))

#freq, lex, sub

#ci dict:
#{0: [['-635.556259815', '-825.916148035'], ['-500.108849475', '-599.246631109'], ['-647.632783115\n', '-741.233461264\n']], 1: [['-168.096670068', '-262.630805218'], ['-271.848659583', '-355.68761216'], ['-213.783588696\n', '-277.169963277\n']], 2: [['-360.599277165', '-482.185485589'], ['-358.293209497', '-454.924436682'], ['-350.455031772\n', '-426.053502528\n']], 3: [['-105.579542801', '-171.053489882'], ['-125.528149438', '-179.222967517'], ['-115.691659856\n', '-164.545794647\n']], 4: [['-340.270991566', '-452.030093796'], ['-338.877504015', '-419.213960233'], ['-327.866293661\n', '-393.554803599\n']], 5: [['-152.405270598', '-228.685009554'], ['-134.35213027', '-184.746104418'], ['-160.469253435\n', '-216.470610255\n']], 6: [['-147.637067095', '-148.307920285'], ['-222.334338066', '-357.034044899'], ['-269.777990552\n', '-292.071097104\n']]}

#outfile = open('2_adult-child_CIs.txt', 'w')
ci_list = dict()
count = 0
for file in file_list:
	freq = []
	lex = []
	sub = []
	for g in file:
		if g[0] == '-':
			x = g.rstrip()
			y = x.split('\t')
			freq.append(y[0])
			lex.append(y[1])
			sub.append(y[2])
	freq.sort()
	lex.sort()
	sub.sort()
	freq_ci = [float(freq[249]),float(freq[9724])]
	lex_ci = [float(lex[249]),float(lex[9724])]
	sub_ci = [float(sub[249]),float(sub[9724])]
	cis = [freq_ci, lex_ci, sub_ci]
	ci_list[count] = cis
	count +=1

countx = 0
for file in mean_list:
	freq = 0
	lex = 0
	sub = 0
	for g in file:
		if g[0] == '-':
			x = g.rstrip()
			y = x.split('\t')
			freq= float(y[0])
			lex= float(y[1])
			sub= float(y[2])	
	temp = ci_list[countx]
	temp.append([freq, lex, sub])
	ci_list[countx] = temp
	countx +=1

temp = ci_list[6]
temp.append([freq_mean, lex_mean, sub_mean])
ci_list[6] = temp

save_object(ci_list, 'ci_info.pkl')

#print('freq, lex, sub')
#print(freq_ci, lex_ci, sub_ci)

#2 yo adult child cis (['-644.422825832', '-834.456125868'], ['-476.054843534', '-568.664436455'], ['-633.215639716\n', '-728.344168194\n'])
#2 yo adult child means [-764.763192322	,-663.306283789	,-814.578912327]
#3 yo means -336.296089012	-436.875670766	-434.785908655
#3 yo cis(['-359.546406719', '-478.447000162'], ['-354.536995875', '-449.937847066'], ['-354.766393975\n', '-431.161846099\n'])
#4 means -379.424232553	-407.26802576	-361.796573284
#4 cis (['-346.040796671', '-462.671032362'], ['-338.242933721', '-416.954297143'], ['-328.155119476\n', '-393.614671803\n'])


#
# freq_ci = [-346.040796671,-462.671032362]
# lex_ci = [-338.242933721, -416.954297143]
# sub_ci = [-328.15511947, -393.614671803]
# x = [1,2,3]
# y_bottom = [float(freq_ci[0]),float(lex_ci[0]), float(sub_ci[0])]
# y_top = [float(freq_ci[1]),float(lex_ci[1]), float(sub_ci[1])]
# x_left = [x[0]-.1, x[1]-.1, x[2]-.1]
# x_right = [x[0]+.1, x[1]+.1, x[2]+.1]
#
# means_adult_adult = [-379.424232553,-407.26802576,-361.796573284]
# objects = ('freq', 'lex', 'sub')
# plt.bar(x, means_adult_adult)
# plt.hlines(y_bottom, x_left, x_right)
# plt.hlines(y_top, x_left, x_right)
# plt.vlines(x, y_bottom, y_top)
# plt.xticks(x, objects)
#
# plt.show()

infile.close()
infile1.close()
infile2.close()
infile3.close()
infile4.close()
infile5.close()
infile6.close()
infile7.close()
infile8.close()
infile9.close()
infile10.close()
infile11.close()
infile12.close()
