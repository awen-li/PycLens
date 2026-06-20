# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_issue1395_5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(self.testdata), encoding='ascii')
    txt._CHUNK_SIZE = 4
    reads = txt.read(4)
    pos = txt.tell()
    txt.seek(0)
    txt.seek(pos)
    self.assertEqual(txt.read(4), 'BBB\n')
