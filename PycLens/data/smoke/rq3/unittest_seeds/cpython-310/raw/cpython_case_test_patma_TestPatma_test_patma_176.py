# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_176

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def whereis(point):
        match point:
            case [0, 0]:
                return 'Origin'
            case [0, y]:
                return f'Y={y}'
            case [x, 0]:
                return f'X={x}'
            case [x, y]:
                return f'X={x}, Y={y}'
            case _:
                return 'Not a point'
    self.assertEqual(whereis((0, 0)), 'Origin')
    self.assertEqual(whereis((0, -1.0)), 'Y=-1.0')
    self.assertEqual(whereis(('X', 0)), 'X=X')
    self.assertEqual(whereis((None, 1j)), 'X=None, Y=1j')
    self.assertEqual(whereis(42), 'Not a point')
