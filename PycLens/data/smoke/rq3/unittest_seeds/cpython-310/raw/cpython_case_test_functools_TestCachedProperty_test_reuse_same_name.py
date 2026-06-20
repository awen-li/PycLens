# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_reuse_same_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    counter = 0

    @py_functools.cached_property
    def _cp(_self):
        nonlocal counter
        counter += 1
        return counter

    class A:
        cp = _cp

    class B:
        cp = _cp
    a = A()
    b = B()
    self.assertEqual(a.cp, 1)
    self.assertEqual(b.cp, 2)
    self.assertEqual(a.cp, 1)
