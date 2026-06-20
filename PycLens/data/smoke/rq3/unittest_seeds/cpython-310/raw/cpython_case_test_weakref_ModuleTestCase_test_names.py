# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ModuleTestCase_test_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for name in ('ReferenceType', 'ProxyType', 'CallableProxyType', 'WeakMethod', 'WeakSet', 'WeakKeyDictionary', 'WeakValueDictionary'):
        obj = getattr(weakref, name)
        if name != 'WeakSet':
            self.assertEqual(obj.__module__, 'weakref')
        self.assertEqual(obj.__name__, name)
        self.assertEqual(obj.__qualname__, name)
