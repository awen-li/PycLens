# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sentinel = object()

    class A:

        def method(self):
            return sentinel

    class C(A):

        def method(self, /):
            return super().method()
    self.assertEqual(C().method(), sentinel)
