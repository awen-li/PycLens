# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_206

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case 1 | 2 | 3:
                out = locals()
                del out['w']
                return out
    self.assertEqual(f(1), {})
    self.assertEqual(f(2), {})
    self.assertEqual(f(3), {})
    self.assertEqual(f(3.0), {})
    self.assertIs(f(0), None)
    self.assertIs(f(4), None)
    self.assertIs(f('1'), None)
