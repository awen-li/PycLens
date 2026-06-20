# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.MockRawIO()
    b = self.tp(raw)
    clsname = '(%s\\.)?%s' % (self.tp.__module__, self.tp.__qualname__)
    self.assertRegex(repr(b), '<%s>' % clsname)
    raw.name = 'dummy'
    self.assertRegex(repr(b), "<%s name='dummy'>" % clsname)
    raw.name = b'dummy'
    self.assertRegex(repr(b), "<%s name=b'dummy'>" % clsname)
