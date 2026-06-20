# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_222

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(x):
        match x:
            case _:
                return 0
    self.assertEqual(f(0), 0)
    self.assertEqual(f(1), 0)
    self.assertEqual(f(2), 0)
    self.assertEqual(f(3), 0)
