# -*- coding: utf-8 -*-
import pandas as pd
import numpy
import sys

from models import session, List, ListItems
#excel导入数据库



#1.将excel文件放在同一文件夹下
#2.将excel各页的名字修改为欲插入的表单组名
#3.每页excel的格式应该是列名为第一行之后就是具体的数据行
#4.希望插入表单项的数据内容应该放在第一列

def excel_inert_mysql(file_name):
	l = pd.read_excel(file_name, sheetname=None)
	for k, v in l.items():
		if k in [u'list_1', u'list_2', u'list_3', u'list_4', u'list_5']:
			l = session.query(List).filter(List.group_name==k).first()
			if not l:
				l = List()
				l.group_name = k
				#db.session.add(l)
				session.add(bl)
				#db.session.commit()
				session.commit()
			list_id = l.list_id

			data = []
			series = v[v.columns[0]].dropna()
			for i in series:
				context = str(numpy.asscalar(i)) if type(i) == numpy.int64 else i
				data.append({'context':context, 'list_id':list_id})
			#db.session.execute(ListItems.__table__.insert().prefix_with('IGNORE').values(data))
			session.execute(ListItems.__table__.insert().prefix_with('IGNORE').values(data))
			#db.session.commit()
			session.commit()

if __name__ == '__main__':
	#python input_excel file_name
	excel_inert_mysql('l.xlsx')

