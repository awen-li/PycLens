# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_211

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case {'x': x, 'y': 'y', 'z': z}:
                out = locals()
                del out['w']
                return out
    self.assertEqual(f({'x': 'x', 'y': 'y', 'z': 'z'}), {'x': 'x', 'z': 'z'})
    self.assertEqual(f({'x': 'x', 'y': 'y', 'z': 'z', 'a': 'a'}), {'x': 'x', 'z': 'z'})
    self.assertIs(f({'x': 'x', 'y': 'yy', 'z': 'z', 'a': 'a'}), None)
    self.assertIs(f({'x': 'x', 'y': 'y'}), None)
