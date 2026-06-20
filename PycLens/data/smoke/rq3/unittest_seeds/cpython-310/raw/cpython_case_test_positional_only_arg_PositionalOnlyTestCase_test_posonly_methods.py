# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_posonly_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Example:

        def f(self, a, b, /):
            return (a, b)
    self.assertEqual(Example().f(1, 2), (1, 2))
    self.assertEqual(Example.f(Example(), 1, 2), (1, 2))
    self.assertRaises(TypeError, Example.f, 1, 2)
    expected = "f\\(\\) got some positional-only arguments passed as keyword arguments: 'b'"
    with self.assertRaisesRegex(TypeError, expected):
        Example().f(1, b=2)
