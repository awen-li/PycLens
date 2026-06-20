# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_112

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:

        class B:
            C = 0
    x = 0
    match x:
        case A.B.C:
            y = 0
    self.assertEqual(A.B.C, 0)
    self.assertEqual(x, 0)
    self.assertEqual(y, 0)
