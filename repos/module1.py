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
        
    def solve(self):
        s = solver()
        count = 1
        con = 0
        while self.check(self.a) and con < 500:
            print(count)
            g = s.get_bin(self.a, count)
            b = s.cut(g)
            c = s.evaluate_bin(b, self.a)
            d = s.cut(c)
            e = s.evaluate_prob(d)
            print(c)
            print(e)
            self.a = s.fill_in(self.a, e, count)
            print(self.a)
            if count < 9:
                count += 1
            elif count == 9:
                count = 1
            con += 1
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

