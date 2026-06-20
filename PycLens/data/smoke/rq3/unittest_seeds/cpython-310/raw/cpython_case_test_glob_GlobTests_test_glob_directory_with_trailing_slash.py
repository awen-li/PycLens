# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_directory_with_trailing_slash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = glob.glob(self.norm('Z*Z') + os.sep)
    self.assertEqual(res, [])
    res = glob.glob(self.norm('ZZZ') + os.sep)
    self.assertEqual(res, [])
    res = glob.glob(self.norm('aa*') + os.sep)
    self.assertEqual(len(res), 2)
    self.assertIn(set(res), [{self.norm('aaa'), self.norm('aab')}, {self.norm('aaa') + os.sep, self.norm('aab') + os.sep}])
