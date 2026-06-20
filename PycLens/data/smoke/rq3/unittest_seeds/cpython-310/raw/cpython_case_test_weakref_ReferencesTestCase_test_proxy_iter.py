# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    obj = None

    class MyObj:

        def __iter__(self):
            nonlocal obj
            del obj
            return NotImplemented
    obj = MyObj()
    p = weakref.proxy(obj)
    with self.assertRaises(TypeError):
        'blech' in p
