# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_getopt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmdline = ['-a', '1', '-b', '--alpha=2', '--beta', '-a', '3', '-a', '', '--beta', 'arg1', 'arg2']
    (opts, args) = getopt.getopt(cmdline, 'a:b', ['alpha=', 'beta'])
    self.assertEqual(opts, [('-a', '1'), ('-b', ''), ('--alpha', '2'), ('--beta', ''), ('-a', '3'), ('-a', ''), ('--beta', '')])
    self.assertEqual(args, ['arg1', 'arg2'])
    self.assertError(getopt.getopt, cmdline, 'a:b', ['alpha', 'beta'])
