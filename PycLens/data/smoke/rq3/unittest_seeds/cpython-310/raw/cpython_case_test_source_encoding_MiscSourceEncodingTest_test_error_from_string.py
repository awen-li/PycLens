# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_source_encoding.py
# case: MiscSourceEncodingTest_test_error_from_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input = '# coding: ascii\n☃'.encode('utf-8')
    with self.assertRaises(SyntaxError) as c:
        compile(input, '<string>', 'exec')
    expected = "'ascii' codec can't decode byte 0xe2 in position 16: ordinal not in range(128)"
    self.assertTrue(c.exception.args[0].startswith(expected), msg=c.exception.args[0])
