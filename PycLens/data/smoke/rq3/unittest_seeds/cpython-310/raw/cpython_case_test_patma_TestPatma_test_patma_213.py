# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_213

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case [p, q] as x:
                out = locals()
                del out['w']
                return out
    self.assertEqual(f((1, 2)), {'p': 1, 'q': 2, 'x': (1, 2)})
    self.assertEqual(f([1, 2]), {'p': 1, 'q': 2, 'x': [1, 2]})
    self.assertIs(f(12), None)
    self.assertIs(f((1, 2, 3)), None)
