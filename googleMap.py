#coding=utf8
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib2
import os, time, logging, json, random


class crawlerQQMap(object):
	def __init__(self):
		
		# google
		self.urlHead = 'https://maps.googleapis.com/maps/api/geocode/json?address='
		self.urlEnd= '&key=YOUROWNKEY'
		self.mdict = {}

	def getLatLng(self, addr):
		addr_after = addr.replace(' ', '')
		if ('香港' in addr_after) == False:
			addr_after = '香港' + addr_after
		print addr_after
		url = '%s%s%s' % (self.urlHead, addr_after, self.urlEnd)
		self.jsonInfo  = urllib2.urlopen(url).read()
		json_text = json.loads(self.i)
		if json_text['status'] == 0:
			lat = json_text['result']['location']['lat']
			lng = json_text['result']['location']['lng']
			self.mdict[addr] = str(lng)+','+str(lat)
			# print self.mdict[addr]
		else:
			self.mdict[addr] = ' , '
		time.sleep(0.2)
		return self.mdict[addr]
	def googlegetLatLng(self, addr):
		addr_after = addr.replace(' ', '')
		if ('香港' in addr_after) == False:
			addr_after = '香港' + addr_after
		# print addr_after
		url = '%s%s%s' % (self.urlHead, addr_after, self.urlEnd)
		self.jsonInfo  = urllib2.urlopen(url).read()
		json_text = json.loads(self.jsonInfo)
		if json_text['status'] == 'OK':
			lat = json_text['results'][0]['geometry']['location']['lat']
			lng = json_text['results'][0]['geometry']['location']['lng']
			self.mdict[addr] = str(lng)+','+str(lat)
			print addr, self.mdict[addr]
		else:
			self.mdict[addr] = ' , '
		time.sleep(0.2)
		return self.mdict[addr]


if __name__ == '__main__':
	logging.basicConfig(
		filename = '%s.txt' % 'log', 
		level=logging.DEBUG, 
		format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s', 
		datefmt='%a, %d %b %Y %H:%M:%S')
	print 'start'
	qq = crawlerQQMap()
	f =open('data/xxxx.txt')
	qq.googlegetLatLng('香港嘉悅半島第一座')
	mlist = []
	for line in f:
		addr = line.strip()
		if qq.mdict.has_key(addr) == False:
			mlist.append(qq.googlegetLatLng(addr))
		else:
			mlist.append(qq.mdict[addr])
	f.close()
	f = open('data/xxxll.txt', 'w')
	f.write('\n'.join(mlist))
	f.close()


