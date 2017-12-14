#!/usr/bin/env python
#-*- coding: utf-8 -*-Nov 24 05:45:22
from datetime import datetime
f = open ('auth.log', 'r')
li = []
chu={}
for linea in f.readlines():
    if 'authentication failure' in linea:
	    li.append(datetime.strptime(linea[:15],'%b %d %H:%M:%S')) 
f.close()
for dat in li:
	print datetime.strftime(dat, '%m %d %H:%M:%S')
