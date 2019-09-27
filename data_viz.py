import matplotlib.pyplot as plt
import sys
import argparse as ap
import math_lib as m
import viz
import numpy as np

def boxplot(L, out_file_name):
	fig, ax = plt.subplots()

	# Draw boxplots, specifying desired style
	ax.boxplot(L)

	# By default, the tick label starts at 1 and increments by 1 for
	# each box drawn. This sets the labels to the ones we want

	title = 'Mean: ' + str(m.list_mean(L)) + ' Stdev: ' + str(m.list_stdev(L))

#	ax.set_xticklabels(L)
	ax.set_ylabel('Value')
#	ax.set_xlabel('stdev')
	ax.set_title(title)
	

	plt.savefig(out_file_name+'.png')
	plt.show()

def histogram(L, out_file_name):
	# create figure and axis
	fig, ax = plt.subplots()
	# plot histogram
	ax.hist(L)
	# set title and labels
	title = 'Mean: ' + str(m.list_mean(L)) + ' Stdev: ' + str(m.list_stdev(L))
	ax.set_title(title)
	ax.set_xlabel('Value')
	ax.set_ylabel('Frequency')
	plt.savefig(out_file_name+'.png')
	plt.show()

def combo(L, out_file_name):
	fig, ax = plt.subplots(2)

	title = 'Mean: ' + str(m.list_mean(L)) + ' Stdev: ' + str(m.list_stdev(L))
	# plot histogram
	ax[1].hist(L)
	# set title and labels
	ax[1].set_title(title)
	ax[1].set_xlabel('Value')
	ax[1].set_ylabel('Frequency')

#	fig, ax = plt.subplots()
	ax[0].boxplot(L)
#	ax[0].set_xticklabels(L)
	ax[0].set_ylabel('Value')
#	ax[0].set_xlabel('stdev')
	ax[0].set_title(title)
	
	plt.savefig(out_file_name+'.png')
	plt.show()


def main(o, plot,data):
	L = data
	print (L)
	out_file_name = o
	if plot == 'histogram':
		histogram(L, out_file_name)
	if plot == 'combo':
		combo(L, out_file_name)
	if plot == 'boxplot':
		boxplot(L, out_file_name)
	
	mean = m.list_mean(L)
if __name__ == '__main__':
    main()

