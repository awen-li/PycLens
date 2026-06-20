# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_eof.py
# case: EOFTestCase_test_eof_with_line_continuation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = 'unexpected EOF while parsing (<string>, line 1)'
    try:
        compile('"\\xhh" \\', '<string>', 'exec', dont_inherit=True)
    except SyntaxError as msg:
        self.assertEqual(str(msg), expect)
    else:
        raise support.TestFailed
