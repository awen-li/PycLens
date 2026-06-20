# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_subn

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.subn('(?i)b+', 'x', 'bbbb BBBB'), ('x x', 2))
    self.assertEqual(re.subn('b+', 'x', 'bbbb BBBB'), ('x BBBB', 1))
    self.assertEqual(re.subn('b+', 'x', 'xyz'), ('xyz', 0))
    self.assertEqual(re.subn('b*', 'x', 'xyz'), ('xxxyxzx', 4))
    self.assertEqual(re.subn('b*', 'x', 'xyz', 2), ('xxxyz', 2))
    self.assertEqual(re.subn('b*', 'x', 'xyz', count=2), ('xxxyz', 2))
