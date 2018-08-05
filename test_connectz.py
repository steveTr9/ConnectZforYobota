import connectz
import unittest
import numpy as np


class TestConnectZ(unittest.TestCase):

    def test_s_int(self):
        self.assertEquals(connectz.s_int(5),5)
        self.assertEquals(connectz.s_int(''),-1)
        self.assertEquals(connectz.s_int(0), 0)


    def test_check_slot(self):
        self.assertEquals(connectz.check_slot(1, np.array([[0, 0, 0],
                                                           [1, 0, 0],
                                                           [1, 2, 0]])),1)
        self.assertEquals(connectz.check_slot(0, np.array([[0, 0, 0],
                                                           [1, 0, 0],
                                                           [1, 2, 0]])), 0)
        self.assertEquals(connectz.check_slot(2, np.array([[0, 0, 0],
                                                           [1, 0, 0],
                                                           [1, 2, 0]])), 2)

    def test_check_win(self):
        self.assertEquals(connectz.check_win(7, np.array([[0, 0, 1],
                                                          [2, 1, 2],
                                                          [1, 2, 1]]), 1, 1, 1, 3), 1)
        self.assertEquals(connectz.check_win(8, np.array([[2, 0, 1],
                                                          [2, 2, 1],
                                                          [1, 1, 2]]), 2, 0, 0, 3), 2)
        self.assertEquals(connectz.check_win(5, np.array([[0, 0, 0],
                                                          [2, 2, 0],
                                                          [1, 1, 1]]), 1, 2, 2, 3), 1)
        self.assertEquals(connectz.check_win(5, np.array([[1, 0, 0],
                                                          [1, 2, 0],
                                                          [1, 2, 0]]), 1, 0, 0, 3), 1)


if __name__ == '__main__':
    unittest.main()