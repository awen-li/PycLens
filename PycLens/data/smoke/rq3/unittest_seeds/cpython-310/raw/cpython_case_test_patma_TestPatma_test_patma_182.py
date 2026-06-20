# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_182

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def whereis(points):
        match points:
            case []:
                return 'No points'
            case [Point(0, 0)]:
                return 'The origin'
            case [Point(x, y)]:
                return f'Single point {x}, {y}'
            case [Point(0, y1), Point(0, y2)]:
                return f'Two on the Y axis at {y1}, {y2}'
            case _:
                return 'Something else'
    self.assertEqual(whereis([]), 'No points')
    self.assertEqual(whereis([Point(0, 0)]), 'The origin')
    self.assertEqual(whereis([Point(0, 1)]), 'Single point 0, 1')
    self.assertEqual(whereis([Point(0, 0), Point(0, 0)]), 'Two on the Y axis at 0, 0')
    self.assertEqual(whereis([Point(0, 1), Point(0, 1)]), 'Two on the Y axis at 1, 1')
    self.assertEqual(whereis([Point(0, 0), Point(1, 0)]), 'Something else')
    self.assertEqual(whereis([Point(0, 0), Point(0, 0), Point(0, 0)]), 'Something else')
    self.assertEqual(whereis([Point(0, 1), Point(0, 1), Point(0, 1)]), 'Something else')
