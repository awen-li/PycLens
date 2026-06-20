# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_reuse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    proxy1 = weakref.proxy(o)
    ref = weakref.ref(o)
    proxy2 = weakref.proxy(o)
    self.assertIs(proxy1, proxy2, 'proxy object w/out callback should have been re-used')
