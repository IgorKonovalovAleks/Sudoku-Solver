#a = np.array([[ 1,  0,  4,  7,  0,  9,  0,  0,  0],
#       [0, 0, 0, 0, 0, 0, 0, 6, 0],
#       [3, 0, 5, 0, 4, 0, 0, 0, 0],
#       [0, 0, 0, 5, 0, 0, 0, 4, 6],
#       [0, 5, 3, 1, 0, 4, 9, 2, 0],
#       [2, 4, 0, 0, 0, 8, 0, 0, 0],
#       [0, 0, 0, 0, 7, 0, 6, 0, 5],
#       [0, 8, 0, 0, 0, 0, 0, 0, 0],
#       [0, 0, 0, 9, 0, 5, 4, 0, 1]])
import numpy as np


class sudoku_solver():

    cube_index = np.array([[[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]],
                       [[0,3], [0,4], [0,5], [1,3], [1,4], [1,5], [2,3], [2,4], [2,5]],
                       [[0,6], [0,7], [0,8], [1,6], [1,7], [1,8], [2,6], [2,7], [2,8]],
                       [[3,0], [3,1], [3,2], [4,0], [4,1], [4,2], [5,0], [5,1], [5,2]],
                       [[3,3], [3,4], [3,5], [4,3], [4,4], [4,5], [5,3], [5,4], [5,5]],
                       [[3,6], [3,7], [3,8], [4,6], [4,7], [4,8], [5,6], [5,7], [5,8]],
                       [[6,0], [6,1], [6,2], [7,0], [7,1], [7,2], [8,0], [8,1], [8,2]],
                       [[6,3], [6,4], [6,5], [7,3], [7,4], [7,5], [8,3], [8,4], [8,5]],
                       [[6,6], [6,7], [6,8], [7,6], [7,7], [7,8], [8,6], [8,7], [8,8]]])

    def __init__(self):
        self.attempt = 0
        self.number = 1

    def fill_in(self, main, prob, number):
        for i in range(9):
            for j in range(9):
                if prob[i, j] == 100:
                    main[i, j] = number
        return main

    def fill(self, main, index):
        main[index[0], index[1]] = self.number
        return main

    def solution(self, main):
        print(self.number)
        print(self.attempt)
        if self.number == 10:
            self.number = 1
            reply = self.solution(main)
            return reply
        probability = self.get_bin(main, self.number)
        cut = self.cut(probability)
        probability = self.evaluate_bin(cut, main)
        cut = self.cut(probability)
        probability = self.evaluate_prob(cut)
        print(probability)
        maximum = np.max(probability)
        if maximum == 0:
            print('no more cells to fill in')
            return None
        print(maximum)
        indeces = list()
        for i in range(9):
            for j in range(9):
                if probability[i, j] == maximum:
                    indeces.append((i, j))
        print(indeces)
        try:
            reply = tuple((indeces[self.attempt][0], indeces[self.attempt][1]))
        except IndexError:
            reply = None
        if self.attempt < len(indeces):
            self.attempt += 1
        else:
            self.number += 1
            reply = self.solution(main)
        return reply

    def evaluate_bin(self, cut, main):
        binnary = np.array([False for i in range(81)]).reshape((9, 9))
        for i in range(27):
            for j in range(9):
                if cut[i, j]:
                    cut[i, 0 : 9] = True
                    break
        for i in range(9):
            for j in range(9):
                if cut[i, j] or cut[j + 9, i] or cut[self.cube_index[i, j, 0] + 18, self.cube_index[i, j, 1]] or main[i, j]:
                    continue
                else:
                    binnary[i, j] = True
        return binnary

    def evaluate_prob(self, cut):
        reply = np.array([0 for i in range(81)]).reshape((9, 9))
        uncollected = np.array([0.0 for i in range(243)]).reshape((27, 9))
        for i in range(27):
            count = np.count_nonzero(cut[i])
            for j in range(9):
                if cut[i, j]:
                    uncollected[i, j] = 100 / count
                else:
                    continue
        for i in range(9):
            for j in range(9):
                if cut[i, j]:
                    row  = uncollected[i, j]
                    line = uncollected[j + 9, i]
                    cube = uncollected[self.cube_index[i, j, 0] + 18, self.cube_index[i, j, 1]]
                    if  row >= line and row >= cube:
                        reply[i, j] = row
                    elif line >= row and line >= cube:
                        reply[i, j] = line
                    elif cube >= row and cube >= line:
                        reply[i, j] = cube
        return reply

    def get_bin(self, arr, n):
        reply = np.array([False for i in range(81)]).reshape((9, 9))
        for i in range(9):
            for j in range(9):
                if arr[i, j] == n:
                    reply[i, j] = True
        return reply

    def cut(self, arr):
    	cut = np.array([False for i in range(243)]).reshape((27, 9))
    	for i in range(9):
    		cut[i] = arr[i]
    	for i in range(9):
    		cut[i + 9] = arr.flat[i::9]
    	for i in range(9):
    		for j in range(9):
    			cut[i + 18, j] = arr[self.cube_index[i, j, 0], self.cube_index[i, j, 1]]
    	return cut

if __name__ == "__main__":
    a = np.array([[ 1,  0,  4,  7,  0,  9,  0,  0,  0],
       [0, 0, 0, 0, 0, 0, 0, 6, 0],
       [3, 0, 5, 0, 4, 0, 0, 0, 0],
       [0, 0, 0, 5, 0, 0, 0, 4, 6],
       [0, 5, 3, 1, 0, 4, 9, 2, 0],
       [2, 4, 0, 0, 0, 8, 0, 0, 0],
       [0, 0, 0, 0, 7, 0, 6, 0, 5],
       [0, 8, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 9, 0, 5, 4, 0, 1]])
    s = sudoku_solver()
    g = s.get_bin(a, 4)
    print(g)
    b = s.cut(g)
    print(b)
    c = s.evaluate_bin(b)
    print(c)
    d = s.cut(c)
    e = s.evaluate_prob(d)
    print(e, d)
    f = s.fill_in(a, e, 4)
    print(f)