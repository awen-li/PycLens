# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_long_has_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (has_arg, option) = getopt.long_has_args('abc', ['abc='])
    self.assertTrue(has_arg)
    self.assertEqual(option, 'abc')
    (has_arg, option) = getopt.long_has_args('abc', ['abc'])
    self.assertFalse(has_arg)
    self.assertEqual(option, 'abc')
    (has_arg, option) = getopt.long_has_args('abc', ['abcd'])
    self.assertFalse(has_arg)
    self.assertEqual(option, 'abcd')
    self.assertError(getopt.long_has_args, 'abc', ['def'])
    self.assertError(getopt.long_has_args, 'abc', [])
    self.assertError(getopt.long_has_args, 'abc', ['abcd', 'abcde'])
