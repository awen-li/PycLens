# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestClassDecorators_test_double

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def ten(x):
        x.extra = 10
        return x

    def add_five(x):
        x.extra += 5
        return x

    @add_five
    @ten
    class C(object):
        pass
    self.assertEqual(C.extra, 15)
