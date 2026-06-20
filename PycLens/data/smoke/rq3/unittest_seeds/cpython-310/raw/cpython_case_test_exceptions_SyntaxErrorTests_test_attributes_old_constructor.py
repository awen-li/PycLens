# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: SyntaxErrorTests_test_attributes_old_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ('bad.py', 1, 2, 'abcdefg')
    the_exception = SyntaxError('bad bad', args)
    (filename, lineno, offset, error) = args
    self.assertEqual(filename, the_exception.filename)
    self.assertEqual(lineno, the_exception.lineno)
    self.assertEqual(None, the_exception.end_lineno)
    self.assertEqual(offset, the_exception.offset)
    self.assertEqual(None, the_exception.end_offset)
    self.assertEqual(error, the_exception.text)
    self.assertEqual('bad bad', the_exception.msg)
