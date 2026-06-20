# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestMutate_test_remove_until_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expected_len = len(self.set)
    for v in self.values:
        self.set.remove(v)
        expected_len -= 1
        self.assertEqual(len(self.set), expected_len)
