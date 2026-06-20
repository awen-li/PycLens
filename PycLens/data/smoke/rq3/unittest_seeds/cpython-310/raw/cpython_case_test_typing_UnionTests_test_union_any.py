# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_union_any

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = Union[Any]
    self.assertEqual(u, Any)
    u1 = Union[int, Any]
    u2 = Union[Any, int]
    u3 = Union[Any, object]
    self.assertEqual(u1, u2)
    self.assertNotEqual(u1, Any)
    self.assertNotEqual(u2, Any)
    self.assertNotEqual(u3, Any)
