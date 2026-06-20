# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_proxy_bad_next

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    not_an_iterator = lambda : 0

    class A:

        def __iter__(self):
            return weakref.proxy(not_an_iterator)
    a = A()
    msg = 'Weakref proxy referenced a non-iterator'
    with self.assertRaisesRegex(TypeError, msg):
        list(a)
