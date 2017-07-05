# -*- coding: utf-8 -*-
import os
import os.path


#文件索引
def index(path):
    if 'main' in path.lower():
        print(path)
    if path == '':
        now = '.'
    else:
        now = path
    menu = os.listdir(now)
    for i in menu:
        if now == '.':
            file = i
        else:
            file = now + i
        if not os.path.isdir(file):
            if i.endswith('.py') or i.endswith('.txt') or i.endswith('.xml'):
                 with open(file) as f:
                    text = f.read()
                    if 'keyword' in text.lower():
                        print(file)
        else:
            if now == '.':
                path = i + '/'
                index(path)
            else:
                path = now + i + '/'
                index(path)

if __name__ == "__main__":
    path = ''
    index(path)