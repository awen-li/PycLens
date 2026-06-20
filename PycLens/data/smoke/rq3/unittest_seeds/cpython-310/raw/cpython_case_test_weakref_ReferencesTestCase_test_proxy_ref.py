# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_ref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = C()
    o.bar = 1
    ref1 = weakref.proxy(o, self.callback)
    ref2 = weakref.proxy(o, self.callback)
    del o
    gc_collect()

    def check(proxy):
        proxy.bar
    self.assertRaises(ReferenceError, check, ref1)
    self.assertRaises(ReferenceError, check, ref2)
    ref3 = weakref.proxy(C())
    gc_collect()
    self.assertRaises(ReferenceError, bool, ref3)
    self.assertEqual(self.cbcalled, 2)
