# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_closures

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(x, y):

        def g(x2, /, y2):
            return x + y + x2 + y2
        return g
    self.assertEqual(f(1, 2)(3, 4), 10)
    with self.assertRaisesRegex(TypeError, "g\\(\\) missing 1 required positional argument: 'y2'"):
        f(1, 2)(3)
    with self.assertRaisesRegex(TypeError, 'g\\(\\) takes 2 positional arguments but 3 were given'):
        f(1, 2)(3, 4, 5)

    def f(x, /, y):

        def g(x2, y2):
            return x + y + x2 + y2
        return g
    self.assertEqual(f(1, 2)(3, 4), 10)

    def f(x, /, y):

        def g(x2, /, y2):
            return x + y + x2 + y2
        return g
    self.assertEqual(f(1, 2)(3, 4), 10)
    with self.assertRaisesRegex(TypeError, "g\\(\\) missing 1 required positional argument: 'y2'"):
        f(1, 2)(3)
    with self.assertRaisesRegex(TypeError, 'g\\(\\) takes 2 positional arguments but 3 were given'):
        f(1, 2)(3, 4, 5)
