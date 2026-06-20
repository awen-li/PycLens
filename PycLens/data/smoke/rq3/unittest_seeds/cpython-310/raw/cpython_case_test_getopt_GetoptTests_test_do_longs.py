# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_do_longs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (opts, args) = getopt.do_longs([], 'abc', ['abc'], [])
    self.assertEqual(opts, [('--abc', '')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_longs([], 'abc=1', ['abc='], [])
    self.assertEqual(opts, [('--abc', '1')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_longs([], 'abc=1', ['abcd='], [])
    self.assertEqual(opts, [('--abcd', '1')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_longs([], 'abc', ['ab', 'abc', 'abcd'], [])
    self.assertEqual(opts, [('--abc', '')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_longs([], 'foo=42', ['foo-bar', 'foo='], [])
    self.assertEqual(opts, [('--foo', '42')])
    self.assertEqual(args, [])
    self.assertError(getopt.do_longs, [], 'abc=1', ['abc'], [])
    self.assertError(getopt.do_longs, [], 'abc', ['abc='], [])
