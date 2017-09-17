#!/usr/bin/env python

import csv

def parseDictionary(fn):
	f_handle = open(fn, 'r')
	reader = csv.reader(f_handle)

	freq_count_dict = {}
	n_words = 0

	for row in reader:
		n_words += 1
		word_length = len(row[0])
		if (word_length in freq_count_dict):
			freq_count_dict[word_length] += 1
		else:
			freq_count_dict[word_length] = 1
	return (freq_count_dict,n_words)

def parseDictionary2(fn):
	f_handle = open(fn, 'r')
	reader = csv.reader(f_handle)

	freq_count_dict = {}
	n_words = 0

	for row in reader:
		n_words += 1
		word_length = len(row[0])
		try:
			freq_count_dict[word_length] += 1
		except KeyError as e:
			freq_count_dict[word_length] = 1
	return (freq_count_dict,n_words)

freq_count_dict,n_words = parseDictionary('dictionary')

# def displayCountDict(freq_count_dict,n_words,max_hist_surface=500):
# 	keys = freq_count_dict.keys()
# 	print keys
# 	symbol_size = n_words / max_hist_surface
# 	for l in keys:
# 		rel_freq = float(freq_count_dict[l]) / n_words
# 		hist_symbols = 'o' * int(round(freq_count_dict[l]/symbol_size))
# 		print "%d:\t%d\t(%f)\t->\t	%s" % (l,freq_count_dict[l],rel_freq,hist_symbols)

# displayCountDict(freq_count_dict,n_words)