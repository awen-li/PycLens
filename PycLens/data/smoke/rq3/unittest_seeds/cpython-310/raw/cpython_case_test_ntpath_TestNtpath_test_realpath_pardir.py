# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_pardir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = ntpath.normpath(os.getcwd())
    tester("ntpath.realpath('..')", ntpath.dirname(expected))
    tester("ntpath.realpath('../..')", ntpath.dirname(ntpath.dirname(expected)))
    tester("ntpath.realpath('/'.join(['..'] * 50))", ntpath.splitdrive(expected)[0] + '\\')
    tester("ntpath.realpath('..\\..')", ntpath.dirname(ntpath.dirname(expected)))
    tester("ntpath.realpath('\\'.join(['..'] * 50))", ntpath.splitdrive(expected)[0] + '\\')
