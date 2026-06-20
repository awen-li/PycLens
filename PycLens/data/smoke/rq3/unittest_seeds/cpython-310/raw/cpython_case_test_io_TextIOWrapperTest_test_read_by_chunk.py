# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_read_by_chunk

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(b'A' * 127 + b'\r\nB'), encoding='utf-8')
    reads = ''
    while True:
        c = txt.read(128)
        if not c:
            break
        reads += c
    self.assertEqual(reads, 'A' * 127 + '\nB')
