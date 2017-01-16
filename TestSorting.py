import unittest
import MapLogic
import ReduceLogic

class WCMapperTest(unittest.TestCase):
    def test_mapper(self):
        input = ['Ana Brennan,7728 Hall,Williamsberg,45095','Tiffany Wilkins,6755 Patricia 57191,Ruthchester,66323','Joe Turner,6755 Patricia 57191,Ruthchester,66323']
        expected = ['045095,Ana Brennan', '066323,Tiffany Wilkins', '066323,Joe Turner']
        result = []
        for output in MapLogic.mapper(input):
            result.append(output)
        self.assertEqual(expected, result)

    def test_reducer(self):
        input = ['045095,Ana Brennan', '066323,Tiffany Wilkins','066323,Joe Turner']
        expected = ['045095\tAna Brennan', '066323\tTiffany Wilkins:Joe Turner']
        result = []
        for output in ReduceLogic.reducer(input):
            result.append(output)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()