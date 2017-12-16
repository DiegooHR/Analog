#!/usr/bin/env python
#-*- coding: utf-8 -*-Nov 24 05:45:22
from datetime import datetime
X = open ('auth.log', 'r')
dic={}
li = []
for linea in f.readlines():
	if 'authentication failure' in linea:
		Y= lista[lista.find('rhost')+4:]
		if Y.split()[0] in linea:
			li=[]
			tiempo=datetime.strptime(linea[:12], '%b %d %H:%M:%S')
			li.append(linea[:12])
			if Y.split[0] not in dic:
				dic[Y.split[0]]=li

log.close()
print dic
