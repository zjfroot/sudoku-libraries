# -*- coding: iso-8859-15 -*-
import sys

class sudoku:
    def new_game(self):
        numbers = [[1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9],
                   [1,2,3,4,5,6,7,8,9]]
        self.print_sudoku(numbers)

    ##todo:
    ##generate distinct random numbers


    def print_sudoku(self,numbers):
        i = j = 0
        while j < 9:
            while i < 9:
                sys.stdout.write(str(numbers[j][i]))
                sys.stdout.write(' ')
                if i == 2 or i == 5:
                    sys.stdout.write(' ')
                if i == 8 and j != 8:
                    print
                i += 1
            if j == 2 or j == 5:
                print
            i = 0
            j += 1

##         print "1 2 3  4 5 6  7 8 9"
##         print "1 2 3  4 5 6  7 8 9"
##         print "1 2 3  4 5 6  7 8 9\n"
##         print "1 2 3  4 5 6  7 8 9"
##         print "1 2 3  4 5 6  7 8 9"
##         print "1 2 3  4 5 6  7 8 9\n"
##         print "1 2 3  4 5 6  7 8 9"
##         print "1 2 3  4 5 6  7 8 9"
##         print "1 2 3  4 5 6  7 8 9"


mysudoku = sudoku()
mysudoku.new_game()


