# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_positional_only_invalid_calls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b, /):
        pass
    f(1, 2)
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'b'"):
        f(1)
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 2 required positional arguments: 'a' and 'b'"):
        f()
    with self.assertRaisesRegex(TypeError, 'f\\(\\) takes 2 positional arguments but 3 were given'):
        f(1, 2, 3)
