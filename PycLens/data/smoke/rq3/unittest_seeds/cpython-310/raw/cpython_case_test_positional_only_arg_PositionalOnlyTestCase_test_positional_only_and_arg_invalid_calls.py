# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_positional_only_and_arg_invalid_calls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b, /, c):
        pass
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'c'"):
        f(1, 2)
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 2 required positional arguments: 'b' and 'c'"):
        f(1)
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 3 required positional arguments: 'a', 'b', and 'c'"):
        f()
    with self.assertRaisesRegex(TypeError, 'f\\(\\) takes 3 positional arguments but 4 were given'):
        f(1, 2, 3, 4)
