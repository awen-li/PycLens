# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_write_fromascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO()
    txt = self.TextIOWrapper(raw, encoding='ascii', newline='\n')
    txt.write('foo\n')
    txt.reconfigure(encoding='utf-8-sig')
    txt.write('é\n')
    txt.flush()
    self.assertEqual(raw.getvalue(), b'foo\n\xc3\xa9\n')
