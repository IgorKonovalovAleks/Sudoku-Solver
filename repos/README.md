# ForExample
Sudoku Solver on Python
There are three python source files. The main file is solve_sudoku.py. But others are also necessary.
Skript solve_sudoku.py takes nine strings from console, makes numpy.ndarray and then brings it to module1.main(your_sudoku).solve().
For example:
Enter one row: 020960001
Enter one row: 009100080
Enter one row: 004027000
Enter one row: 000603002
Enter one row: 130000054
Enter one row: 200504000
Enter one row: 000230500
Enter one row: 050009700
Enter one row: 900051040

When sudoku solving will be done, you should see the result:
Result:
[[5. 2. 3. 9. 6. 8. 4. 7. 1.]
 [6. 7. 9. 1. 4. 5. 2. 8. 3.]
 [8. 1. 4. 3. 2. 7. 9. 6. 5.]
 [4. 8. 5. 6. 7. 3. 1. 9. 2.]
 [1. 3. 7. 8. 9. 2. 6. 5. 4.]
 [2. 9. 6. 5. 1. 4. 8. 3. 7.]
 [7. 4. 8. 2. 3. 6. 5. 1. 9.]
 [3. 5. 1. 4. 8. 9. 7. 2. 6.]
 [9. 6. 2. 7. 5. 1. 3. 4. 8.]]
