# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        m = self._view(tp(self._source))
        for tp_comp in self._types:
            self.assertTrue(m == tp_comp(b'abcdef'))
            self.assertFalse(m != tp_comp(b'abcdef'))
            self.assertFalse(m == tp_comp(b'abcde'))
            self.assertTrue(m != tp_comp(b'abcde'))
            self.assertFalse(m == tp_comp(b'abcde1'))
            self.assertTrue(m != tp_comp(b'abcde1'))
        self.assertTrue(m == m)
        self.assertTrue(m == m[:])
        self.assertTrue(m[0:6] == m[:])
        self.assertFalse(m[0:5] == m)
        self.assertFalse(m == 'abcdef')
        self.assertTrue(m != 'abcdef')
        self.assertFalse('abcdef' == m)
        self.assertTrue('abcdef' != m)
        for c in (m, b'abcdef'):
            self.assertRaises(TypeError, lambda : m < c)
            self.assertRaises(TypeError, lambda : c <= m)
            self.assertRaises(TypeError, lambda : m >= c)
            self.assertRaises(TypeError, lambda : c > m)
