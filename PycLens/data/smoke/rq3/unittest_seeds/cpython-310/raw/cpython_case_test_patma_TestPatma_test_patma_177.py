# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_177

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def whereis(point):
        match point:
            case Point(0, 0):
                return 'Origin'
            case Point(0, y):
                return f'Y={y}'
            case Point(x, 0):
                return f'X={x}'
            case Point():
                return 'Somewhere else'
            case _:
                return 'Not a point'
    self.assertEqual(whereis(Point(1, 0)), 'X=1')
    self.assertEqual(whereis(Point(0, 0)), 'Origin')
    self.assertEqual(whereis(10), 'Not a point')
    self.assertEqual(whereis(Point(False, False)), 'Origin')
    self.assertEqual(whereis(Point(0, -1.0)), 'Y=-1.0')
    self.assertEqual(whereis(Point('X', 0)), 'X=X')
    self.assertEqual(whereis(Point(None, 1j)), 'Somewhere else')
    self.assertEqual(whereis(Point), 'Not a point')
    self.assertEqual(whereis(42), 'Not a point')
