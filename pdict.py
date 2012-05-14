#!/usr/bin/python
#

import urllib, sys
from xml.etree.ElementTree import parse

def dict_tran(word):
	dict_cn_url = "http://dict.cn/ws.php?utf8=true&q=%s" % word
	dict_cn_xml = parse(urllib.urlopen(dict_cn_url)).getroot()
	pron = dict_cn_xml.find("pron")
	define = dict_cn_xml.find("def")
	if define == None:
		print "word '%s' not found T_T" % word
	else:
		if pron != None:
			print "pronunciation: /", pron.text, "/"
		print "definitions: "
		print define.text

def youdao_tran(word):
	youdao_url = "http://fanyi.youdao.com/openapi.do?keyfrom=chaoswork&key=1495522961&type=data&doctype=xml&version=1.1&q=%s" % word
#	fd = urllib.urlopen(youdao_url)
#	print fd.read()
	exs = parse(urllib.urlopen(youdao_url)).getroot().findall("basic/explains/ex")
	for ex in exs:
		print ex.text


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "usage: pdict.py <word>"
	else:
		word = ' '.join(sys.argv[1:len(sys.argv)])
		print word
		dict_tran(word)
		youdao_tran(word)
