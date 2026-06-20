# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestNamedTuple_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = TestNT(x=10, y=20, z=30)
    for copier in (copy.copy, copy.deepcopy):
        q = copier(p)
        self.assertEqual(p, q)
        self.assertEqual(p._fields, q._fields)
