# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_210

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(w):
        match w:
            case [x, y, z]:
                out = locals()
                del out['w']
                return out
    self.assertEqual(f((1, 2, 3)), {'x': 1, 'y': 2, 'z': 3})
    self.assertIs(f((1, 2)), None)
    self.assertIs(f((1, 2, 3, 4)), None)
    self.assertIs(f(123), None)
    self.assertIs(f('abc'), None)
    self.assertIs(f(b'abc'), None)
    self.assertEqual(f(array.array('b', b'abc')), {'x': 97, 'y': 98, 'z': 99})
    self.assertEqual(f(memoryview(b'abc')), {'x': 97, 'y': 98, 'z': 99})
    self.assertIs(f(bytearray(b'abc')), None)
