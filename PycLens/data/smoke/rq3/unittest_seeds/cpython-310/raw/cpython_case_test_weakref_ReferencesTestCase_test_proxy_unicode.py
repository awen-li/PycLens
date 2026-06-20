# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __str__(self):
            return 'string'

        def __bytes__(self):
            return b'bytes'
    instance = C()
    self.assertIn('__bytes__', dir(weakref.proxy(instance)))
    self.assertEqual(bytes(weakref.proxy(instance)), b'bytes')
