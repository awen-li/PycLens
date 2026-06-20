# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_113

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        class B:
            C = 0
            D = 1
    x = 1
    match x:
        case A.B.C:
            y = 0
        case A.B.D:
            y = 1
    self.assertEqual(A.B.C, 0)
    self.assertEqual(A.B.D, 1)
    self.assertEqual(x, 1)
    self.assertEqual(y, 1)
