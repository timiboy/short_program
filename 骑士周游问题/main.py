# -*-coding:utf-8-*-
import time

class Stack():
	def __init__(self):
		self._elems = []

	def is_empty(self):
		return self._elems == []

	def top(self):
		if self.is_empty():
			raise ValueError('empty')
		return self._elems[-1]

	def push(self, elem):
		self._elems.append(elem)

	def pop(self):
		if self.is_empty():
			raise ValueError('empty')
		return self._elems.pop()

	def __len__(self):
		return len(self._elems)

	def __str__(self):
		return str([each[0] for each in self._elems])


class Queue():
	def __init__(self, init_len=8):
		self._elems = [0] * 8
		self._head = 0
		self._len = 8
		self._num = 0

	def is_empty(self):
		return self._num == 0

	def top(self):
		if self.is_empty():
			raise ValueError('empty')
		return self._elems[self._head]

	def dequeue(self):
		if self.is_empty():
			raise ValueError('empty')
		e = self._elems[self._head]
		self._head = (self._head+1) % self._len
		self._num -= 1
		return e

	def enqueue(self, elem):
		if self._num == self._len:
			self._extend()
		self._elems[(self._head+self._num) % self._len] = elem
		self._num += 1

	def _extend(self):
		new_len = self._len * 2
		new_elems = [0] * new_len
		for i in range(0, self._num):
			new_elems[i] = self._elems[(self._head+i) % self._len]
		self._len = new_len
		self._elems = new_elems

chessboard = []
for i in range(8):
	chessboard.append([0] * 8)

chessboard2 = []
for i in range(8):
	chessboard2.append([0] * 8)


dist = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

def inboard(chessboard, pos):
	if pos[0] < 0 or \
		pos[1] < 0 or \
		pos[0] >= len(chessboard) or\
		pos[1] >= len(chessboard[pos[0]]):
		return False
	return True

def setable(chessboard, pos):
	if chessboard[pos[0]][pos[1]] != 0:
		return False
	return True

def mark(chessboard, pos):
	chessboard[pos[0]][pos[1]] = 1

def clean_mark(chessboard, pos):
	chessboard[pos[0]][pos[1]] = 0

def chess_place(chessboard, pos):
	return chessboard[pos[0]][pos[1]] == 1

def get_weight(chessboard, pos):
	weight = 0
	for x, y in dist:
		nextp = (pos[0]+x, pos[1]+y)
		if inboard(chessboard, nextp) and setable(chessboard, nextp):
			weight += 1
	return weight

# 递归求解
# 使用改进方案， 每次向前看两步并计算每种下一步情况可能的走法（定义为权值）， 之后从可能情况数少的开始递归
def set_pieces(chessboard, pos, path):
	mark(chessboard, pos)
	path.append(pos)
	if len(path) >= len(chessboard) ** 2:
		return True
	nextp_weight = []
	for x, y in dist:
		nextp = (pos[0]+x, pos[1]+y)
		if inboard(chessboard, nextp):
			if setable(chessboard, nextp):
				nextp_weight.append((nextp, get_weight(chessboard, nextp)))
	nextp_weight = sorted(nextp_weight, key=lambda x:x[1])
	for nextp, weight in nextp_weight:
		if set_pieces(chessboard, nextp, path):
			return True
		else:
			clean_mark(chessboard, nextp)
			path.remove(nextp)
	return False

path = []
print set_pieces(chessboard2, (0, 0), path)
for num, pos in enumerate(path):
	chessboard2[pos[0]][pos[1]] = num
for each in chessboard2:
	print each

print '==================================='
# 堆栈非递归求解
def set_pieces(chessboard, start, pieces):
	s = Stack()
	s.push((start, 0))
	while not s.is_empty():
		if len(s) >= len(chessboard) ** 2:
			pieces.append(str(s))
		pos, dir = s.pop()
		if chess_place(chessboard, pos):
			clean_mark(chessboard, pos)
		for i in range(dir, 8):
			nextp = (pos[0]+dist[i][0], pos[1]+dist[i][1])
			if inboard(chessboard, nextp) and setable(chessboard, nextp):
				s.push((pos, i+1))
				mark(chessboard, pos)
				s.push((nextp, 0))
				break
	if len(pieces) > 0:
		for each in pieces:
			print each
		return True
	return False

# print set_pieces(chessboard, (0, 0), [])






