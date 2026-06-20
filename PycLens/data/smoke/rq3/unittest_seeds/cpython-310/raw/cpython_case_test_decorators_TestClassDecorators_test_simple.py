# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestClassDecorators_test_simple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def plain(x):
        x.extra = 'Hello'
        return x

    @plain
    class C(object):
        pass
    self.assertEqual(C.extra, 'Hello')
