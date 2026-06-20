# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_gnu_getopt

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cmdline = ['-a', 'arg1', '-b', '1', '--alpha', '--beta=2']
    (opts, args) = getopt.gnu_getopt(cmdline, 'ab:', ['alpha', 'beta='])
    self.assertEqual(args, ['arg1'])
    self.assertEqual(opts, [('-a', ''), ('-b', '1'), ('--alpha', ''), ('--beta', '2')])
    (opts, args) = getopt.gnu_getopt(['-a', '-', '-b', '-'], 'ab:', [])
    self.assertEqual(args, ['-'])
    self.assertEqual(opts, [('-a', ''), ('-b', '-')])
    (opts, args) = getopt.gnu_getopt(cmdline, '+ab:', ['alpha', 'beta='])
    self.assertEqual(opts, [('-a', '')])
    self.assertEqual(args, ['arg1', '-b', '1', '--alpha', '--beta=2'])
    self.env['POSIXLY_CORRECT'] = '1'
    (opts, args) = getopt.gnu_getopt(cmdline, 'ab:', ['alpha', 'beta='])
    self.assertEqual(opts, [('-a', '')])
    self.assertEqual(args, ['arg1', '-b', '1', '--alpha', '--beta=2'])
