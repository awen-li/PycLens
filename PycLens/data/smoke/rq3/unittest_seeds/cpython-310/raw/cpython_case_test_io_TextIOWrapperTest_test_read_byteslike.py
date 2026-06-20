# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_read_byteslike

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = MemviewBytesIO(b'Just some random string\n')
    t = self.TextIOWrapper(r, 'utf-8')
    bytes_val = _to_memoryview(r.getvalue()).tobytes()
    self.assertEqual(t.read(200), bytes_val.decode('utf-8'))
