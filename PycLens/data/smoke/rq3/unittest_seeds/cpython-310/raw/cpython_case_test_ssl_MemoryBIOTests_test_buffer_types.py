# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: MemoryBIOTests_test_buffer_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = ssl.MemoryBIO()
    bio.write(b'foo')
    self.assertEqual(bio.read(), b'foo')
    bio.write(bytearray(b'bar'))
    self.assertEqual(bio.read(), b'bar')
    bio.write(memoryview(b'baz'))
    self.assertEqual(bio.read(), b'baz')
