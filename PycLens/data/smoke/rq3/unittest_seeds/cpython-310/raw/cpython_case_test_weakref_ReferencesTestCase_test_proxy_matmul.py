# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_matmul

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __matmul__(self, other):
            return 1729

        def __rmatmul__(self, other):
            return -163

        def __imatmul__(self, other):
            return 561
    o = C()
    p = weakref.proxy(o)
    self.assertEqual(p @ 5, 1729)
    self.assertEqual(5 @ p, -163)
    p @= 5
    self.assertEqual(p, 561)
