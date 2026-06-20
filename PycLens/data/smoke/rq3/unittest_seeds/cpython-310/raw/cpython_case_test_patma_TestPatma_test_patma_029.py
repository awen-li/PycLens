# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_029

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = {}
    y = None
    match x:
        case {0: [1, 2, {}]}:
            y = 0
        case {0: [1, 2, {}], 1: [[]]}:
            y = 1
        case []:
            y = 2
    self.assertEqual(x, {})
    self.assertIs(y, None)
