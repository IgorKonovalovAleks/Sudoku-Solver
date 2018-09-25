import module1
import numpy as np

flag = False
c = 0
sud = np.zeros(81).reshape((9, 9))

while flag == False:
    for c in range(9):
        row = input('Enter one row: ')
        count = 0
        for i in row:
            sud[c, count] = int(row[count])
            count += 1

    print(sud)
    repeat = input('Is that right?(yes/no)')
    if repeat == 'yes':
        flag = True
    else:
        flag = False

solver = module1.main(sud)
answer = solver.solve()
print('\n')
print('Result:')
print(answer)
