from main import sudoku


class sudokuTester:

    def test_r(self):
        mysudoku = sudoku()
        kkk = 0
        while kkk < 8:
            print mysudoku.r([1,2,3,4,5,6,7,8,9])
            kkk += 1



t = sudokuTester()
t.test_r()
