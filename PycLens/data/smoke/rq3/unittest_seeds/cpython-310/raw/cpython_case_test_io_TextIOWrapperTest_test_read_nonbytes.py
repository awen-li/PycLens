# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_read_nonbytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.TextIOWrapper(self.StringIO('a'), encoding='utf-8')
    self.assertRaises(TypeError, t.read, 1)
    t = self.TextIOWrapper(self.StringIO('a'), encoding='utf-8')
    self.assertRaises(TypeError, t.readline)
    t = self.TextIOWrapper(self.StringIO('a'), encoding='utf-8')
    self.assertRaises(TypeError, t.read)
