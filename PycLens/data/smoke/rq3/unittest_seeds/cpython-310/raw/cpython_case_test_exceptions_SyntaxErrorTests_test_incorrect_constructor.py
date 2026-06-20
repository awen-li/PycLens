# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: SyntaxErrorTests_test_incorrect_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    args = ('bad.py', 1, 2)
    self.assertRaises(TypeError, SyntaxError, 'bad bad', args)
    args = ('bad.py', 1, 2, 4, 5, 6, 7)
    self.assertRaises(TypeError, SyntaxError, 'bad bad', args)
    args = ('bad.py', 1, 2, 'abcdefg', 1)
    self.assertRaises(TypeError, SyntaxError, 'bad bad', args)
