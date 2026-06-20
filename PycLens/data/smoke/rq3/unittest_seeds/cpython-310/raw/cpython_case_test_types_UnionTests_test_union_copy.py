# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_union_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = list[T] | int
    for copied in (copy.copy(orig), copy.deepcopy(orig)):
        self.assertEqual(copied, orig)
        self.assertEqual(copied.__args__, orig.__args__)
        self.assertEqual(copied.__parameters__, orig.__parameters__)
