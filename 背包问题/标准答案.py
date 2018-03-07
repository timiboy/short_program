# -*- coding:utf-8 -*-


import random

def knap_rec(weight, wlist, n):
	if weight == 0:
		return True
	if weight < 0 or (weight > 0 and n < 1):
		return False
	if knap_rec(weight-wlist[n-1], wlist, n-1):
		print 'Item' + str(n-1) + ':' + str(wlist[n-1]) + ' ',
		return True
	if knap_rec(weight, wlist, n-1):
		return True
	else:
		return False

if __name__ == '__main__':
	weight = 97
	wlist = {i:random.randint(1, 20) for i in range(20)}
	print knap_rec(weight, wlist, len(wlist))