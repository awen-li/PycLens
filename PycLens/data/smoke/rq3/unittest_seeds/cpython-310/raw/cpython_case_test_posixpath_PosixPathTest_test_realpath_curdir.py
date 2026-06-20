# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_realpath_curdir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(realpath('.'), os.getcwd())
    self.assertEqual(realpath('./.'), os.getcwd())
    self.assertEqual(realpath('/'.join(['.'] * 100)), os.getcwd())
    self.assertEqual(realpath(b'.'), os.getcwdb())
    self.assertEqual(realpath(b'./.'), os.getcwdb())
    self.assertEqual(realpath(b'/'.join([b'.'] * 100)), os.getcwdb())
