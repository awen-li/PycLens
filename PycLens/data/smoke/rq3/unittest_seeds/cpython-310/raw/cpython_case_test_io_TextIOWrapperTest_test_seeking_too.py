# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_seeking_too

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'\xe0\xbf\xbf\n'
    with self.open(os_helper.TESTFN, 'wb') as f:
        f.write(data)
    with self.open(os_helper.TESTFN, 'r', encoding='utf-8') as f:
        f._CHUNK_SIZE
        f._CHUNK_SIZE = 2
        f.readline()
        f.tell()
