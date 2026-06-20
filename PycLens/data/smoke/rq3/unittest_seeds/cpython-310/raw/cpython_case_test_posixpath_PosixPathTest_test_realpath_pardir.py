# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_pardir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(realpath('..'), dirname(os.getcwd()))
    self.assertEqual(realpath('../..'), dirname(dirname(os.getcwd())))
    self.assertEqual(realpath('/'.join(['..'] * 100)), '/')
    self.assertEqual(realpath(b'..'), dirname(os.getcwdb()))
    self.assertEqual(realpath(b'../..'), dirname(dirname(os.getcwdb())))
    self.assertEqual(realpath(b'/'.join([b'..'] * 100)), b'/')
