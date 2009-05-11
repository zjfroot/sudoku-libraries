from main import sudoku
from misc import Tools

class SudokuTester:

    def test_r(self):
        mysudoku = sudoku()
        kkk = 0
        while kkk < 8:
            print mysudoku.r([1,2,3,4,5,6,7,8,9])
            kkk += 1

    def test_tools_r(self):
        tool = Tools()
        kkk = 0
        while kkk < 8:
            print tool.r([1,2,3,4,5,6,7,8,9])
            kkk += 1

    def test_tools_r_locations(self):
        tool = Tools()
        print tool.r_locations([1,2,3,4,5,6,7,8,9],4)
        
t = SudokuTester()
#t.test_r()
#t.test_tools_r()
t.test_tools_r_locations()
