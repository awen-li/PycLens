# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_183

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def whereis(point):
        match point:
            case Point(x, y) if x == y:
                return f'Y=X at {x}'
            case Point(x, y):
                return 'Not on the diagonal'
    self.assertEqual(whereis(Point(0, 0)), 'Y=X at 0')
    self.assertEqual(whereis(Point(0, False)), 'Y=X at 0')
    self.assertEqual(whereis(Point(False, 0)), 'Y=X at False')
    self.assertEqual(whereis(Point(-1 - 1j, -1 - 1j)), 'Y=X at (-1-1j)')
    self.assertEqual(whereis(Point('X', 'X')), 'Y=X at X')
    self.assertEqual(whereis(Point('X', 'x')), 'Not on the diagonal')
