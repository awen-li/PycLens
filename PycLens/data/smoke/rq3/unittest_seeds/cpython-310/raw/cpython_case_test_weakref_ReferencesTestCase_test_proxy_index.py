# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __index__(self):
            return 10
    o = C()
    p = weakref.proxy(o)
    self.assertEqual(operator.index(p), 10)
