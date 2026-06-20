# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_do_shorts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (opts, args) = getopt.do_shorts([], 'a', 'a', [])
    self.assertEqual(opts, [('-a', '')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_shorts([], 'a1', 'a:', [])
    self.assertEqual(opts, [('-a', '1')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_shorts([], 'a', 'a:', ['1'])
    self.assertEqual(opts, [('-a', '1')])
    self.assertEqual(args, [])
    (opts, args) = getopt.do_shorts([], 'a', 'a:', ['1', '2'])
    self.assertEqual(opts, [('-a', '1')])
    self.assertEqual(args, ['2'])
    self.assertError(getopt.do_shorts, [], 'a1', 'a', [])
    self.assertError(getopt.do_shorts, [], 'a', 'a:', [])
