# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_reversed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyObj:

        def __len__(self):
            return 3

        def __reversed__(self):
            return iter('cba')
    obj = MyObj()
    self.assertEqual(''.join(reversed(weakref.proxy(obj))), 'cba')
