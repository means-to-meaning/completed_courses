#!/usr/bin/env python

import urllib2
import requests
from HTMLParser import HTMLParser


class MyHTMLParser(HTMLParser):

	def handle_starttag(self, tag, attrs):
		print("Start tag: " + tag)

	def handle_endtag(self, tag):
		print("End tag: " + tag)

	def handle_data(self, data):
		# if not str(data).startswith('\n'):
		print("Data: " + repr(data))

	def handle_comment(self,comment):
		print("Comment" + comment)

response = urllib2.urlopen('http://good-eland-3116.vagrantshare.com')
html = response.read()

parser = MyHTMLParser()
parser.feed(html)
print html


# foo = requests.get('http://good-eland-3116.vagrantshare.com')
# print foo.headers
# print foo.text

# url = 'http://www.gwndwn.org.uk/toxml.php'
# data = {"somekey": "somevalue"}

# foo = requests.get(url,data=data)
# print foo.headers
# print foo.text


