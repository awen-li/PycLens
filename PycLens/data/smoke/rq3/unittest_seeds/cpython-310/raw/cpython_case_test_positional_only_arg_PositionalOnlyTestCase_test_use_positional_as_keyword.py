# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_use_positional_as_keyword

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, /):
        pass
    expected = "f\\(\\) got some positional-only arguments passed as keyword arguments: 'a'"
    with self.assertRaisesRegex(TypeError, expected):
        f(a=1)

    def f(a, /, b):
        pass
    expected = "f\\(\\) got some positional-only arguments passed as keyword arguments: 'a'"
    with self.assertRaisesRegex(TypeError, expected):
        f(a=1, b=2)

    def f(a, b, /):
        pass
    expected = "f\\(\\) got some positional-only arguments passed as keyword arguments: 'a, b'"
    with self.assertRaisesRegex(TypeError, expected):
        f(a=1, b=2)
