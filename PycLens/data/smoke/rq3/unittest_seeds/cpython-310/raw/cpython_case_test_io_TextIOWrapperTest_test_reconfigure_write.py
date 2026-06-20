# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO()
    txt = self.TextIOWrapper(raw, encoding='latin1', newline='\n')
    txt.write('abcé\n')
    txt.reconfigure(encoding='utf-8')
    self.assertEqual(raw.getvalue(), b'abc\xe9\n')
    txt.write('déf\n')
    txt.flush()
    self.assertEqual(raw.getvalue(), b'abc\xe9\nd\xc3\xa9f\n')
    raw = self.BytesIO()
    txt = self.TextIOWrapper(raw, encoding='ascii', newline='\n')
    txt.write('abc\n')
    txt.reconfigure(encoding='utf-8-sig')
    txt.write('déf\n')
    txt.flush()
    self.assertEqual(raw.getvalue(), b'abc\nd\xc3\xa9f\n')
