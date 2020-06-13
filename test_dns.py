#!/usr/bin/env python
#coding:utf-8

from socket import gethostbyname
DOMAIN= 'C:/Users/cui/Desktop/domain.txt'
result = 'C:/Users/cui/Desktop/result.txt'
with open(DOMAIN,'r') as f:

     for line in f.readlines():
        try:
            host = gethostbyname(line.strip('\n'))
        except Exception as e:
            with open(result,'a+') as r:
                r.write(line.strip('\n') + ' ')
                r.write('no_ip_return' + '\n')
        else:
            with open(result,'a+') as r:
                r.write(line.strip('\n') + ' ')
                r.write(host + '\n')