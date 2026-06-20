# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_no_standard_args_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b, /, *, c):
        pass
    f(1, 2, c=3)
    with self.assertRaises(TypeError):
        f(1, b=2, c=3)
