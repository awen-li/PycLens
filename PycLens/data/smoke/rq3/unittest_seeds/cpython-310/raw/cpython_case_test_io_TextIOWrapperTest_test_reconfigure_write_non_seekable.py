# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_reconfigure_write_non_seekable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    raw = self.BytesIO()
    raw.seekable = lambda : False
    raw.seek = None
    txt = self.TextIOWrapper(raw, encoding='ascii', newline='\n')
    txt.write('abc\n')
    txt.reconfigure(encoding='utf-8-sig')
    txt.write('déf\n')
    txt.flush()
    self.assertEqual(raw.getvalue(), b'abc\n\xef\xbb\xbfd\xc3\xa9f\n')
