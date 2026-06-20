# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_033

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = []
    match x:
        case {0: [1, 2, {}]}:
            y = 0
        case {0: [1, 2, {}], 1: [[]]}:
            y = 1
        case []:
            y = 2
    self.assertEqual(x, [])
    self.assertEqual(y, 2)
