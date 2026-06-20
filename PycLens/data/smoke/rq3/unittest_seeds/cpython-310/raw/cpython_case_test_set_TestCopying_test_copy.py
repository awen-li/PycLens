# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestCopying_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dup = self.set.copy()
    dup_list = sorted(dup, key=repr)
    set_list = sorted(self.set, key=repr)
    self.assertEqual(len(dup_list), len(set_list))
    for i in range(len(dup_list)):
        self.assertTrue(dup_list[i] is set_list[i])
