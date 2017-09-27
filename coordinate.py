# -*- coding:utf8 -*-
import requests
import json

# ip 或 地址 映射到 经纬度 API
# key 是在百度API中心申请
def coordinate_api(address='', ip='', key=''):
	address_api = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s&ret_coordtype=bd09ll'
	ip_api = 'http://api.map.baidu.com/location/ip?ip=%s&ak=%s&coor=bd09ll'
	if address and ip:
		return json.dumps({'code':-2, 'message':u'ip和address只能输入一个参数'})
	if not (address or ip):
		return json.dumps({'code':-2, 'message':u'ip和address应该至少输入一个参数'})
	if address:
		uri = address_api % (address, key)
		resp = requests.get(uri)
		data = json.loads(resp.text)
		if data.get('status', -2) == 0:
			data = data.get('result', {}).get('location', {})
			return json.dumps({'code':0, 'data':{'latitude':data.get('lat', None), 'longitude':data.get('lng', None)}})
		else:
			return json.dumps({'code':-2, 'message':u'查询出错'})
	elif ip:
		uri = ip_api % (ip, key)
		resp = requests.get(uri)
		data = json.loads(resp.text)
		if data.get('status', -2) == 0:
			data = data.get('content', {}).get('point', {})
			return json.dumps({'code':0, 'data':{'latitude':data.get('y', None), 'longitude':data.get('x', None)}})
		else:
			return json.dumps({'code':-2, 'message':u'查询出错'})


if __name__ == '__main__':
	print coordinate_api(address=u'广东省深圳市会展中心')
	print coordinate_api(ip='153.3.236.12')
