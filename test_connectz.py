import connectz
import unittest


class TestConnectZ(unittest.TestCase):

    def test_s_int(self):
        self.assertEqual(connectz.s_int(5),5)
        self.assertEqual(connectz.s_int(''),-1)
        self.assertEqual(connectz.s_int(0), 0)

    def test_check_win_swne(self):
        self.assertEqual(connectz.check_win_swne(7, {0:[1,2,0],
                                                      1:[2,1,0],
                                                      2:[1,2,1]}, 1, 1, 1, 3, 3), 1)

    def test_check_win(self):
        self.assertEqual(connectz.check_win(7, {0:[1,2,0],1:[2,1,0],2:[1,2,1]}, 1, 1, 1, 3, 3), 1)
        self.assertEqual(connectz.check_win(8, {0:[1,2,2],
                                                 1:[1,2,0],
                                                 2:[2,1,1]}, 2, 0, 2, 3, 3), 2)
        self.assertEqual(connectz.check_win(5, {0:[1,2,0],
                                                 1:[1,2,0],
                                                 2:[1,0,0]}, 1, 2, 0, 3, 3), 1)
        self.assertEqual(connectz.check_win(5, {0:[1,1,1],
                                                 1:[2,2,0],
                                                 2:[0,0,0]}, 1, 0, 2, 3, 3), 1)
        self.assertEqual(connectz.check_win(18, {0:[1,2,0,0,0,0],
                                                  1:[1,2,1,0,0,0],
                                                  2:[2,1,2,0,0,0],
                                                  3:[1,2,2,2,1,0],
                                                  4:[1,1,1,2,2,0],
                                                  5:[0,0,0,0,0,0],
                                                  6:[0,0,0,0,0,0]},2,4,4,4,7),2)


if __name__ == '__main__':
    unittest.main()