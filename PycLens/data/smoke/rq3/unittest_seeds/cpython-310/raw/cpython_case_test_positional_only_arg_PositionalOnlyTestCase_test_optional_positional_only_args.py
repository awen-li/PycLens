# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_optional_positional_only_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b=10, /, c=100):
        return a + b + c
    self.assertEqual(f(1, 2, 3), 6)
    self.assertEqual(f(1, 2, c=3), 6)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got some positional-only arguments passed as keyword arguments: 'b'"):
        f(1, b=2, c=3)
    self.assertEqual(f(1, 2), 103)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got some positional-only arguments passed as keyword arguments: 'b'"):
        f(1, b=2)
    self.assertEqual(f(1, c=2), 13)

    def f(a=1, b=10, /, c=100):
        return a + b + c
    self.assertEqual(f(1, 2, 3), 6)
    self.assertEqual(f(1, 2, c=3), 6)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got some positional-only arguments passed as keyword arguments: 'b'"):
        f(1, b=2, c=3)
    self.assertEqual(f(1, 2), 103)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got some positional-only arguments passed as keyword arguments: 'b'"):
        f(1, b=2)
    self.assertEqual(f(1, c=2), 13)
