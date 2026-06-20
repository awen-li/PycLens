# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_134

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = collections.defaultdict(int, {0: 1})
    match x:
        case {1: 0}:
            y = 0
        case {0: 0}:
            y = 1
        case {**z}:
            y = 2
    self.assertEqual(x, {0: 1})
    self.assertEqual(y, 2)
    self.assertEqual(z, {0: 1})
