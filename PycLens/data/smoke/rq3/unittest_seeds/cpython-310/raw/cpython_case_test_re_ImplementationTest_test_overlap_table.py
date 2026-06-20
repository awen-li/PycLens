# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ImplementationTest_test_overlap_table

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = sre_compile._generate_overlap_table
    self.assertEqual(f(''), [])
    self.assertEqual(f('a'), [0])
    self.assertEqual(f('abcd'), [0, 0, 0, 0])
    self.assertEqual(f('aaaa'), [0, 1, 2, 3])
    self.assertEqual(f('ababba'), [0, 0, 1, 2, 0, 1])
    self.assertEqual(f('abcabdac'), [0, 0, 0, 1, 2, 0, 1, 0])
