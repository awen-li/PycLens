# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestCopying_test_deep_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dup = copy.deepcopy(self.set)
    dup_list = sorted(dup, key=repr)
    set_list = sorted(self.set, key=repr)
    self.assertEqual(len(dup_list), len(set_list))
    for i in range(len(dup_list)):
        self.assertEqual(dup_list[i], set_list[i])
