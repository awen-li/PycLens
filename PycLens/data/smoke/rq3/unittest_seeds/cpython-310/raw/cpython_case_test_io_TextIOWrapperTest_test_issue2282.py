# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_issue2282

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buffer = self.BytesIO(self.testdata)
    txt = self.TextIOWrapper(buffer, encoding='ascii')
    self.assertEqual(buffer.seekable(), txt.seekable())
