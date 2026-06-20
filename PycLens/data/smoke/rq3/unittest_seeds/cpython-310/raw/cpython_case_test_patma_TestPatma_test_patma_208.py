# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_208

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case x:
                out = locals()
                del out['w']
                return out
    self.assertEqual(f(42), {'x': 42})
    self.assertEqual(f((1, 2)), {'x': (1, 2)})
    self.assertEqual(f(None), {'x': None})
