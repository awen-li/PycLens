# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO('hello'.encode('utf-8'))
    b = self.BufferedReader(raw)
    t = self.TextIOWrapper(b, encoding='utf-8')
    modname = self.TextIOWrapper.__module__
    self.assertRegex(repr(t), "<(%s\\.)?TextIOWrapper encoding='utf-8'>" % modname)
    raw.name = 'dummy'
    self.assertRegex(repr(t), "<(%s\\.)?TextIOWrapper name='dummy' encoding='utf-8'>" % modname)
    t.mode = 'r'
    self.assertRegex(repr(t), "<(%s\\.)?TextIOWrapper name='dummy' mode='r' encoding='utf-8'>" % modname)
    raw.name = b'dummy'
    self.assertRegex(repr(t), "<(%s\\.)?TextIOWrapper name=b'dummy' mode='r' encoding='utf-8'>" % modname)
    t.buffer.detach()
    repr(t)
