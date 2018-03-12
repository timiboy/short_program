# -*-coding:utf-8-*-

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
		return str(self._elems)


chessboard = []
for i in range(8):
	chessboard.append([0] * 8)

dist = [(-1, -1), (0, -1), (0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1)]

def get_newchessboard():
	chessboard = []
	for i in range(8):
		chessboard.append([0] * 8)
	return chessboard


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
	chessboard[pos[0]][pos[1]] += 1
	for x, y in dist:
		_pos = (pos[0] + x, pos[1] + y)
		while inboard(chessboard, _pos):
			chessboard[_pos[0]][_pos[1]] += 1
			_pos = (_pos[0] + x, _pos[1] + y)

def clean_mark(chessboard, pos):
	chessboard[pos[0]][pos[1]] -= 1
	for x, y in dist:
		_pos = (pos[0] + x, pos[1] + y)
		while inboard(chessboard, _pos):
			chessboard[_pos[0]][_pos[1]] -= 1
			_pos = (_pos[0] + x, _pos[1] + y)

# 递归求解
def set_pieces(pos, pieces, chessboard):
	if len(pieces) >= 8:
		return True
	elif not inboard(chessboard, pos):
		return False
	nextp = (pos[0] + 1, 0) if pos[1] >= len(chessboard[pos[0]]) - 1 else (pos[0], pos[1] + 1)
	if setable(chessboard, pos):
		mark(chessboard, pos)
		pieces.append(pos)
 		if set_pieces(nextp, pieces, chessboard):
			return True
		else:
			clean_mark(chessboard, pos)
			pieces.remove(pos)
	return set_pieces(nextp, pieces, chessboard)

pieces = []
print set_pieces((0, 0), pieces, chessboard)
for each in chessboard:
	print each


# 非递归求解
def set_pieces(pos, pieces, chessboard):
	s = Stack()
	s.push(pos)
	chess_place = []
	while not s.is_empty():
		pos = s.pop()
		if not inboard(chessboard, pos):
			if s.is_empty():
				break
			pos = s.pop()
			clean_mark(chessboard, pos)
		if pos in chess_place:
			chess_place.remove(pos)
		elif setable(chessboard, pos):
			s.push(pos)
			mark(chessboard, pos)
			chess_place.append(pos)
			if len(s) == 8:
				pieces.append(str(s))
				pos = s.pop()
				clean_mark(chessboard, pos)
		nextp = (pos[0], pos[1]+1) if pos[1] < len(chessboard)-1 else (pos[0]+1, 0)
		s.push(nextp)
	if len(pieces) > 0:
		print len(pieces)
		return True
	else:
		return False

# print set_pieces((0, 0), [], chessboard)