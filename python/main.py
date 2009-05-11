# -*- coding: iso-8859-15 -*-
import sys
import random
from misc import Tools

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

    ## sudoku: a list to represent a soduku
    ## location: 0 1 2 ... 8, which block to populate
    ## limit: how many numbers to populate
    def populate_block(self,sudoku,location,limit):
        t = Tools()
        locations = t.r_locations([1,2,3,4,5,6,7,8,9],limit)
        if location == 0:
            pass
        elif location == 1:
            pass
        else:
            pass

    ## return the random number from a list
    #def r(self,within_list):
    #    return random.choice(within_list) 

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
        print

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
##mysudoku.new_game()
##mysudoku.test_r()
