#!/usr/bin/env python

ip_hostname_dict = {"192.168.1.1": "www.google.com", "10.0.0.1": "www.amazon.com"}

def getAdress(addr, ip_hostname_dict):
	if addr.startswith("www") and addr in ip_hostname_dict.values():
		return ip_hostname_dict.keys()[ip_hostname_dict.values().index(addr)]
	elif addr in ip_hostname_dict:
		return ip_hostname_dict.get(addr)
	else:
		return None

print(getAdress("www.amazon.com",ip_hostname_dict))
print(getAdress("www.yahoo.com",ip_hostname_dict))
print(getAdress("192.168.1.1",ip_hostname_dict))
print(getAdress("192.168.1.2",ip_hostname_dict))

def printDictSummary(word_dict):
	total_occurences = sum(word_dict.values())
	if word_dict:
		for word, occurences in word_dict.items():
			rel_frequency = float(occurences)/total_occurences
			# print word
			# print rel_frequency
			print "word: {}, freq: {}".format(word, rel_frequency)
			# print("%s: %f" % word rel_frequency)
	else:
		print("Dictionary empty!")

wd = {"apple":2, "banana": 3}
printDictSummary(wd)

def wordCounter():
	word_dict = {}
	while True:
		new_word = raw_input("Add a word, write \'STATUS\' for dictionary summary or \'q\' to exit.")
		if new_word == 'STATUS':
			printDictSummary(word_dict)
			continue
		elif new_word == 'q':
			break
		if new_word in word_dict:
			word_dict[new_word] += 1
		else:
			word_dict[new_word] = 1

wordCounter()