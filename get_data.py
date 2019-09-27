import numpy as np
import sys
import os
import pipes
import viz

def read_stdin_col(col_num):
	words = []
	words2 = []
	x = 0
	for line in sys.stdin:
		line = line.split(" ")
#		x = int(line[:1])
		words.append(float(line[col_num]))
		
#		data = [elem.strip().split(',') for elem in words2]
#	line[1:2].strip('\n')
#	words = [float(i) for i in words]
#	print(words)
	return words

def main(data, col_num):
	read_stdin_col(col_num)

if __name__ == '__main__':
    main()

