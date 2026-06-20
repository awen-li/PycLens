# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_eof.py
# case: EOFTestCase_test_line_continuation_EOF

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expect = 'unexpected EOF while parsing (<string>, line 1)'
    with self.assertRaises(SyntaxError) as excinfo:
        exec('x = 5\\')
    self.assertEqual(str(excinfo.exception), expect)
    with self.assertRaises(SyntaxError) as excinfo:
        exec('\\')
    self.assertEqual(str(excinfo.exception), expect)
