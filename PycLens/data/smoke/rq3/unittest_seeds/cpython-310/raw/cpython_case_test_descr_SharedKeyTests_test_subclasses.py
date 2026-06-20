# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: SharedKeyTests_test_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass

    class B(A):
        pass
    (a, b) = (A(), B())
    self.assertEqual(sys.getsizeof(vars(a)), sys.getsizeof(vars(b)))
    self.assertLess(sys.getsizeof(vars(a)), sys.getsizeof({'a': 1}))
    (a.x, a.y, a.z, a.w, a.v, a.u) = range(6)
    self.assertNotEqual(sys.getsizeof(vars(a)), sys.getsizeof(vars(b)))
    a2 = A()
    self.assertEqual(sys.getsizeof(vars(a)), sys.getsizeof(vars(a2)))
    self.assertLess(sys.getsizeof(vars(a)), sys.getsizeof({'a': 1}))
    (b.u, b.v, b.w, b.t, b.s, b.r) = range(6)
    self.assertLess(sys.getsizeof(vars(b)), sys.getsizeof({'a': 1}))
