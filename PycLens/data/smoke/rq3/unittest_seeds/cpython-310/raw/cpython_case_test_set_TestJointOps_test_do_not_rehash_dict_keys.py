# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_do_not_rehash_dict_keys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 10
    d = dict.fromkeys(map(HashCountingInt, range(n)))
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    s = self.thetype(d)
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    s.difference(d)
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    if hasattr(s, 'symmetric_difference_update'):
        s.symmetric_difference_update(d)
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    d2 = dict.fromkeys(set(d))
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    d3 = dict.fromkeys(frozenset(d))
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    d3 = dict.fromkeys(frozenset(d), 123)
    self.assertEqual(sum((elem.hash_count for elem in d)), n)
    self.assertEqual(d3, dict.fromkeys(d, 123))
