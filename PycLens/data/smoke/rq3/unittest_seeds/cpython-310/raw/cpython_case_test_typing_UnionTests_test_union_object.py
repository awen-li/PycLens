# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_union_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = Union[object]
    self.assertEqual(u, object)
    u1 = Union[int, object]
    u2 = Union[object, int]
    self.assertEqual(u1, u2)
    self.assertNotEqual(u1, object)
    self.assertNotEqual(u2, object)
