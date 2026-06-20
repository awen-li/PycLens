# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_issue25862

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.TextIOWrapper(self.BytesIO(b'test'), encoding='ascii')
    t.read(1)
    t.read()
    t.tell()
    t = self.TextIOWrapper(self.BytesIO(b'test'), encoding='ascii')
    t.read(1)
    t.write('x')
    t.tell()
