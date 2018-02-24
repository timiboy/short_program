# -*- coding:utf-8 -*-
import execjs

with open('rsa.js', 'r') as f:
    js_str = f.read()
# 原JS代码中含有navigator变量，所以需要使用浏览器框架phantomjs，也可以选择删去js代码中navigator相关的部分之后直接execjs.compile
js = execjs.get('PhantomJS').compile(js_str)
print js.call('run', 'password')

