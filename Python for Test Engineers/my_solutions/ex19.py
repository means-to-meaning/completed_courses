#!/usr/bin/env python

import urllib2
import requests
from HTMLParser import HTMLParser

import argparse
parser = argparse.ArgumentParser(description="HTML parser for web hosts", epilog="Everything is parsed now!")
# positional, required, no additional argument
parser.add_argument("IP", type=str, help="Address of the website to parser")
# positional, required, additional argument - nonsense all positionals are arguments themselves!
# 
# positional, optional, no additional argument ??
parser.add_argument("IP2", type=str, help="Address2 of the website to parser")
# positional, optional, additional argument - nonsense all positionals are arguments themselves!
# 
# named, optional, no additional argument
parser.add_argument("-v", "--verbose",required=False, help="Add verbose output to the results", action="store_true")
# named, optional, additional argument ?? do we have to add a default value?
parser.add_argument("-d", "--data-tag",required=False, help="Custom string to label data tags",nargs=1)
# named, required, no additional argument - nonsense doesn't add any new information to the script
#
# named, required, additional argument
parser.add_argument("-t", "--startstop-tag",required=True, help="Custom string to label start and stop tags",nargs=2)


args = parser.parse_args()


class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		if args.startstop_tag:
			print(args.startstop_tag + ": " + tag)
		else:
			print("Start tag: " + tag)

	def handle_endtag(self, tag):
		if args.startstop_tag:
			print(args.startstop_tag + ": " + tag)
		else:
			print("End tag: " + tag)

	def handle_data(self, data):
		if args.data_tag:
			print(args.data_tag + ": " + tag)
		else:
			if not str(data).startswith('\n'):
				print("Data: " + repr(data))

	def handle_comment(self,comment):
		print("Comment" + comment)

response = urllib2.urlopen(args.IP)
html = response.read()

print args.verbose
if args.verbose:
	print("Adding a verbose output.")
parser = MyHTMLParser()
parser.feed(html)
# print html