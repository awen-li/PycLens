# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_bytes_directory_with_trailing_slash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = glob.glob(os.fsencode(self.norm('Z*Z') + os.sep))
    self.assertEqual(res, [])
    res = glob.glob(os.fsencode(self.norm('ZZZ') + os.sep))
    self.assertEqual(res, [])
    res = glob.glob(os.fsencode(self.norm('aa*') + os.sep))
    self.assertEqual(len(res), 2)
    self.assertIn(set(res), [{os.fsencode(self.norm('aaa')), os.fsencode(self.norm('aab'))}, {os.fsencode(self.norm('aaa') + os.sep), os.fsencode(self.norm('aab') + os.sep)}])
