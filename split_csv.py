import pandas as pd

#切分csv文件
file_list = pd.read_csv('file_list.csv', index_col=False)
length = len(file_list)
if length == length // 100000:
    length = length // 100000
else:
    length = length // 100000 + 1
for i in range(length):
    bl = file_list.ix[i*100000 : (i+1)*100000]
    bl.to_csv('file_list/fl_%d.csv' % i)
