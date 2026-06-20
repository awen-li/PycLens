# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_204

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case 42:
                out = locals()
                del out['w']
                return out
    self.assertEqual(f(42), {})
    self.assertIs(f(0), None)
    self.assertEqual(f(42.0), {})
    self.assertIs(f('42'), None)
