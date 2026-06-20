# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ntpath.py
# case: TestNtpath_test_realpath_curdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected = ntpath.normpath(os.getcwd())
    tester("ntpath.realpath('.')", expected)
    tester("ntpath.realpath('./.')", expected)
    tester("ntpath.realpath('/'.join(['.'] * 100))", expected)
    tester("ntpath.realpath('.\\.')", expected)
    tester("ntpath.realpath('\\'.join(['.'] * 100))", expected)
