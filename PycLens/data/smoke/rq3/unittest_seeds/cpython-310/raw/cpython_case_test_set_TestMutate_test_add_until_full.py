# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestMutate_test_add_until_full

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tmp = set()
    expected_len = 0
    for v in self.values:
        tmp.add(v)
        expected_len += 1
        self.assertEqual(len(tmp), expected_len)
    self.assertEqual(tmp, self.set)
