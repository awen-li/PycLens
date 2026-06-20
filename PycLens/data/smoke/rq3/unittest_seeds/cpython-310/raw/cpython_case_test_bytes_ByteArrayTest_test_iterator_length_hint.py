# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_iterator_length_hint

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ba = bytearray(b'ab')
    it = iter(ba)
    next(it)
    ba.clear()
    self.assertEqual(list(it), [])
