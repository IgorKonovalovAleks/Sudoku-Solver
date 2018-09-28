import numpy as np
from _sudoku import sudoku_solver as solver


class main():

    a = np.array([[ 0,  2,  0,  9,  6,  0,  0,  0,  1],
       [0, 0, 9, 1, 0, 0, 0, 8, 0],
       [0, 0, 4, 0, 2, 7, 0, 0, 0],
       [0, 0, 0, 6, 0, 3, 0, 0, 2],
       [1, 3, 0, 0, 0, 0, 0, 5, 4],
       [2, 0, 0, 5, 0, 4, 0, 0, 0],
       [0, 0, 0, 2, 3, 0, 5, 0, 0],
       [0, 5, 0, 0, 0, 9, 7, 0, 0],
       [9, 0, 0, 0, 5, 1, 0, 4, 0]])

    def check(self, array):
        for i in range(9):
            for j in range(9):
                if array[i, j] == 0:
                    return True
        return False
    
    def __init__(self, main):
        self.a = main
        self.shadow = self.a.copy()
        self.last = self.a.copy()
        
    def solve(self):
        s = solver()
        count = 1
        con = 0
        while self.check(self.a) and con < 500:
            print(count)
            for i in range(9):
                probability = s.get_bin(self.a, i)
                cut = s.cut(probability)
                probability = s.evaluate_bin(cut, self.a)
                cut = s.cut(probability)
                probability = s.evaluate_prob(cut)
                self.a = s.fill_in(self.a, probability, i)
            if np.allclose(self.a, self.shadow):
                self.last = self.a.copy()
                reply = s.solution(self.a)
                print(reply)
            print(self.a)
            self.shadow = self.a.copy()
        return self.a

if __name__ == "__main__":
    a = np.array([[ 0,  2,  0,  9,  6,  0,  0,  0,  1],
       [0, 0, 9, 1, 0, 0, 0, 8, 0],
       [0, 0, 4, 0, 2, 7, 0, 0, 0],
       [0, 0, 0, 6, 0, 3, 0, 0, 2],
       [1, 3, 0, 0, 0, 0, 0, 5, 4],
       [2, 0, 0, 5, 0, 4, 0, 0, 0],
       [0, 0, 0, 2, 3, 0, 5, 0, 0],
       [0, 5, 0, 0, 0, 9, 7, 0, 0],
       [9, 0, 0, 0, 5, 1, 0, 4, 0]])
    print('hello')
    m = main(a)
    print(m.solve())

