# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tp = self.ro_type
    if tp is None:
        self.skipTest('no read-only type to test')
    b = tp(self._source)
    m = self._view(b)
    self.assertEqual(hash(m), hash(b'abcdef'))
    m.release()
    self.assertEqual(hash(m), hash(b'abcdef'))
    m = self._view(b)
    m.release()
    self.assertRaises(ValueError, hash, m)
