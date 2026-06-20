# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_div

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __floordiv__(self, other):
            return 42

        def __ifloordiv__(self, other):
            return 21
    o = C()
    p = weakref.proxy(o)
    self.assertEqual(p // 5, 42)
    p //= 5
    self.assertEqual(p, 21)
