# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestClassDecorators_test_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def applied_first(x):
        x.extra = 'first'
        return x

    def applied_second(x):
        x.extra = 'second'
        return x

    @applied_second
    @applied_first
    class C(object):
        pass
    self.assertEqual(C.extra, 'second')
