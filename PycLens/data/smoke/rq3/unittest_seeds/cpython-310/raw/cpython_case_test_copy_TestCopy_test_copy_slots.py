# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copy.py
# case: TestCopy_test_copy_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        __slots__ = ['foo']
    x = C()
    x.foo = [42]
    y = copy.copy(x)
    self.assertIs(x.foo, y.foo)
