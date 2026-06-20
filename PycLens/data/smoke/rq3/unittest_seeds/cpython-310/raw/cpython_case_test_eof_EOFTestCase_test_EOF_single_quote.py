# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_eof.py
# case: EOFTestCase_test_EOF_single_quote

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = 'unterminated string literal (detected at line 1) (<string>, line 1)'
    for quote in ("'", '"'):
        try:
            eval(f'{quote}this is a test                ')
        except SyntaxError as msg:
            self.assertEqual(str(msg), expect)
            self.assertEqual(msg.offset, 1)
        else:
            raise support.TestFailed
