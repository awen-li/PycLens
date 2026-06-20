# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_read_one_by_one

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(b'AA\r\nBB'), encoding='utf-8')
    reads = ''
    while True:
        c = txt.read(1)
        if not c:
            break
        reads += c
    self.assertEqual(reads, 'AA\nBB')
