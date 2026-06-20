# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_tobytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for tp in self._types:
        m = self._view(tp(self._source))
        b = m.tobytes()
        expected = b''.join((self.getitem_type(bytes([c])) for c in b'abcdef'))
        self.assertEqual(b, expected)
        self.assertIsInstance(b, bytes)
