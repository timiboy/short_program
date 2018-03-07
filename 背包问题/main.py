# -*- coding:utf-8 -*-
import random

# 背包问题

# 递归方式实现
def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    elif weight > 0 and n >= 0:
        if knap_rec(weight-wlist[n], wlist, n-1):
            # print str(wlist[n])+', ',
            return True
        if knap_rec(weight, wlist, n-1):
            return True
        else:
            return False
    elif (weight > 0 and n < 0) or weight < 0:
        return False


# 非递归方式实现
class Stack():
    def __init__(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        if self.is_empty():
            raise ValueError('stack is empty')
        return self._elems[-1]

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self.is_empty():
            raise ValueError('stack is empty')
        return self._elems.pop()

    # 专门为了背包问题而建立的方法
    def amount(self, wlist):
        return sum(wlist[i] for i in self._elems)

    def show(self, wlist):
        for each in self._elems:
            print 'Item %s: %s' % (str(each), str(wlist[each]))

    def __len__(self):
        return len(self._elems)

def knap_rec_2(weight, wlist, n):
    i = n - 1
    s = Stack()
    while not (i < 0 and s.is_empty()):
        while s.amount(wlist) < weight and i >= 0:
            s.push(i)
            i -= 1
        if len(s) == n and s.amount(wlist) < weight:
            return False
        if s.amount(wlist) > weight:
            i = s.pop()
            i -= 1
        elif s.amount(wlist) < weight and i < 0:
            i = s.pop()
            i -= 1
        elif s.amount(wlist) == weight:
            # s.show(wlist)
            return True
    return False



if __name__ == '__main__':
    weight = 97
    wlist = {i:random.randint(1, 20) for i in range(20)}
    print wlist
    print knap_rec(weight, wlist, len(wlist)-1)
    print knap_rec_2(weight, wlist, len(wlist))

    for i in range(100000):
        print i
        wlist = {i: random.randint(1, 20) for i in range(20)}
        if knap_rec(weight, wlist, len(wlist)-1) != knap_rec(weight, wlist, len(wlist)-1):
            print wlist
            break