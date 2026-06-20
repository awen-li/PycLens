# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_deletion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        result = None

        def __delitem__(self, accessor):
            self.result = accessor
    g = Foo()
    f = weakref.proxy(g)
    del f[0]
    self.assertEqual(f.result, 0)
