# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_eof.py
# case: EOFTestCase_test_EOFS

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = 'unterminated triple-quoted string literal (detected at line 1) (<string>, line 1)'
    try:
        eval("'''this is a test")
    except SyntaxError as msg:
        self.assertEqual(str(msg), expect)
        self.assertEqual(msg.offset, 1)
    else:
        raise support.TestFailed
