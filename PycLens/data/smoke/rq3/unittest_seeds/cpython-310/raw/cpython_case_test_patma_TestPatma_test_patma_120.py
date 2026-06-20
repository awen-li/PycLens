# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_120

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = collections.defaultdict(int)
    match x:
        case {0: 0}:
            y = 0
        case {**z}:
            y = 1
    self.assertEqual(x, {})
    self.assertEqual(y, 1)
    self.assertEqual(z, {})
