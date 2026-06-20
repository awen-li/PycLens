# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_zip_longest_tuple_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ids = list(map(id, zip_longest('abc', 'def')))
    self.assertEqual(min(ids), max(ids))
    ids = list(map(id, list(zip_longest('abc', 'def'))))
    self.assertEqual(len(dict.fromkeys(ids)), len(ids))
