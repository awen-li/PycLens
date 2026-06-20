# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_positional_only_and_kwonlyargs_invalid_calls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b, /, c, *, d, e):
        pass
    f(1, 2, 3, d=1, e=2)
    with self.assertRaisesRegex(TypeError, "missing 1 required keyword-only argument: 'd'"):
        f(1, 2, 3, e=2)
    with self.assertRaisesRegex(TypeError, "missing 2 required keyword-only arguments: 'd' and 'e'"):
        f(1, 2, 3)
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'c'"):
        f(1, 2)
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 2 required positional arguments: 'b' and 'c'"):
        f(1)
    with self.assertRaisesRegex(TypeError, " missing 3 required positional arguments: 'a', 'b', and 'c'"):
        f()
    with self.assertRaisesRegex(TypeError, 'f\\(\\) takes 3 positional arguments but 6 positional arguments \\(and 2 keyword-only arguments\\) were given'):
        f(1, 2, 3, 4, 5, 6, d=7, e=8)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got an unexpected keyword argument 'f'"):
        f(1, 2, 3, d=1, e=4, f=56)
