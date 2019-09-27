import matplotlib.pyplot as plt
import sys
import argparse as ap
import data_viz
import numpy as np
import get_data


def parse():  # parses arguments
    parser = ap.ArgumentParser()

    parser.add_argument('-Out File:',
                        '--out_file',
                        type=str,
                        required=True)

    parser.add_argument('-Plot Type:',
                        '--plot_type',
                        type=str,
                        required=True)

    return parser.parse_args()




def main():
	data = []
	col_num = 0
	am = parse()
	o = am.out_file
	plot = am.plot_type
	data = get_data.read_stdin_col(col_num)
#	read(data)
#	print(data)
	data_viz.main(o, plot, data)

if __name__ == '__main__':
	main()
