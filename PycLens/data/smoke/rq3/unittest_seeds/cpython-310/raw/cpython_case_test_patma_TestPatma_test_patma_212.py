# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_212

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case Point(int(xx), y='hello'):
                out = locals()
                del out['w']
                return out
    self.assertEqual(f(Point(42, 'hello')), {'xx': 42})
