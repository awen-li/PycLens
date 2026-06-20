# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_getopt.py
# case: GetoptTests_test_issue4629

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (longopts, shortopts) = getopt.getopt(['--help='], '', ['help='])
    self.assertEqual(longopts, [('--help', '')])
    (longopts, shortopts) = getopt.getopt(['--help=x'], '', ['help='])
    self.assertEqual(longopts, [('--help', 'x')])
    self.assertRaises(getopt.GetoptError, getopt.getopt, ['--help='], '', ['help'])
