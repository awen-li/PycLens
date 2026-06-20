# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_optparse.py
# case: TestOptionParser_test_get_option

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opt1 = self.parser.get_option('-v')
    self.assertIsInstance(opt1, Option)
    self.assertEqual(opt1._short_opts, ['-v', '-n'])
    self.assertEqual(opt1._long_opts, ['--verbose', '--noisy'])
    self.assertEqual(opt1.action, 'store_true')
    self.assertEqual(opt1.dest, 'verbose')
