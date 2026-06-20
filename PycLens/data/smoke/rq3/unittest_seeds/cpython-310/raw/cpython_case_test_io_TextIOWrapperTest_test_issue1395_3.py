# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_issue1395_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    txt = self.TextIOWrapper(self.BytesIO(self.testdata), encoding='ascii')
    txt._CHUNK_SIZE = 4
    reads = txt.read(4)
    reads += txt.read(4)
    reads += txt.readline()
    reads += txt.readline()
    reads += txt.readline()
    self.assertEqual(reads, self.normalized)
