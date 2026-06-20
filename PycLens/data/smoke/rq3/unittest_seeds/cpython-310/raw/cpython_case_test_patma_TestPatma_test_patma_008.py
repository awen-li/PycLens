# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_008

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 0

    class A:
        y = 1
    match x:
        case A.y as z:
            pass
    self.assertEqual(x, 0)
    self.assertEqual(A.y, 1)
