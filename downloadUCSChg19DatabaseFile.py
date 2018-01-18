import sys
import argparse
import urllib.request
import urllib.parse
import urllib.error
import gzip
#!/usr/bin/env python
# -*- coding: utf-8 -*-


def Main():
	listOfArguements=[]
	parser=argparse.ArgumentParser(description='This is a tool to retrieve annotations from ucsc repository')
	parser.add_argument('--typeOfDatabase',nargs='?')
	args=parser.parse_args()
	return args
	
if __name__=='__main__':
	Main()
	
def extractFileSupplied():
	allReturned=[]
	allReturned=Main()
	typeOfDBUrl=allReturned.typeOfDatabase
	generalUrl='http://hgdownload.soe.ucsc.edu/goldenPath/hg19/database/'
	specificUrl=typeOfDBUrl+".txt.gz"
	url=generalUrl+specificUrl
	return url


def writeTheFileSupliedtoNewFile():	
	allReturned=[]
	allReturned=Main()
	typeOfDBUrl=allReturned.typeOfDatabase
	url=extractFileSupplied()
	print(url)
	specificUrl=typeOfDBUrl+".txt.gz"
	urllib.request.urlretrieve(url, specificUrl)
	f=urllib.request.urlopen(url)	
	data=f.read()
	file=specificUrl
	with open(file,'wb') as code:
		code.write(data)
		

writeTheFileSupliedtoNewFile()