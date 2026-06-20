# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_181

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def whereis(point):
        match point:
            case Point(y=var, x=1):
                return var
    self.assertEqual(whereis(Point(1, 0)), 0)
    self.assertIs(whereis(Point(0, 0)), None)
