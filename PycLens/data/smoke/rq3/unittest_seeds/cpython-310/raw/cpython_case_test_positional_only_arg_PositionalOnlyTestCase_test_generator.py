# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a=1, /, b=2):
        yield (a, b)
    with self.assertRaisesRegex(TypeError, "f\\(\\) got some positional-only arguments passed as keyword arguments: 'a'"):
        f(a=1, b=2)
    gen = f(1, 2)
    self.assertEqual(next(gen), (1, 2))
    gen = f(1, b=2)
    self.assertEqual(next(gen), (1, 2))
    gen = f(1)
    self.assertEqual(next(gen), (1, 2))
    gen = f()
    self.assertEqual(next(gen), (1, 2))
