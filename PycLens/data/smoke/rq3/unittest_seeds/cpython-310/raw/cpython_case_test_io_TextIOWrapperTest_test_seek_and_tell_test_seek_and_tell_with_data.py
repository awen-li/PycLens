# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_seek_and_tell_test_seek_and_tell_with_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.open(os_helper.TESTFN, 'wb')
    f.write(data)
    f.close()
    f = self.open(os_helper.TESTFN, encoding='test_decoder')
    f._CHUNK_SIZE = CHUNK_SIZE
    decoded = f.read()
    f.close()
    for i in range(min_pos, len(decoded) + 1):
        for j in [1, 5, len(decoded) - i]:
            f = self.open(os_helper.TESTFN, encoding='test_decoder')
            self.assertEqual(f.read(i), decoded[:i])
            cookie = f.tell()
            self.assertEqual(f.read(j), decoded[i:i + j])
            f.seek(cookie)
            self.assertEqual(f.read(), decoded[i:])
            f.close()
