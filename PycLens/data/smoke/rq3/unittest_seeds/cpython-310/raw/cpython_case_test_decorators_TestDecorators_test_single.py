# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_single

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        @staticmethod
        def foo():
            return 42
    self.assertEqual(C.foo(), 42)
    self.assertEqual(C().foo(), 42)
