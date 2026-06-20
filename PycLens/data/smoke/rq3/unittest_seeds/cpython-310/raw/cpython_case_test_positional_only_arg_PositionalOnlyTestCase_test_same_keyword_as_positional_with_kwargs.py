# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_same_keyword_as_positional_with_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(something, /, **kwargs):
        return (something, kwargs)
    self.assertEqual(f(42, something=42), (42, {'something': 42}))
    with self.assertRaisesRegex(TypeError, "f\\(\\) missing 1 required positional argument: 'something'"):
        f(something=42)
    self.assertEqual(f(42), (42, {}))
