# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_009

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        B = 0
    match 0:
        case x if x:
            z = 0
        case _ as y if y == x and y:
            z = 1
        case A.B:
            z = 2
    self.assertEqual(A.B, 0)
    self.assertEqual(x, 0)
    self.assertEqual(y, 0)
    self.assertEqual(z, 2)
