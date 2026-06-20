# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_032

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {False: (True, 2.0, {}), 1: [[]], 2: 0}
    match x:
        case {0: [1, 2]}:
            y = 0
        case {0: [1, 2, {}], 1: [[]]}:
            y = 1
        case []:
            y = 2
    self.assertEqual(x, {False: (True, 2.0, {}), 1: [[]], 2: 0})
    self.assertEqual(y, 1)
