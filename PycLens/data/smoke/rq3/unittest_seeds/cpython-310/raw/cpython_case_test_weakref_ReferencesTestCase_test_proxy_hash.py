# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyObj:

        def __hash__(self):
            return 42
    obj = MyObj()
    with self.assertRaises(TypeError):
        hash(weakref.proxy(obj))

    class MyObj:
        __hash__ = None
    obj = MyObj()
    with self.assertRaises(TypeError):
        hash(weakref.proxy(obj))
