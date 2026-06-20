# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_change_default_pos_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b=2, /, c=3):
        return a + b + c
    self.assertEqual((2, 3), f.__defaults__)
    f.__defaults__ = (1, 2, 3)
    self.assertEqual(f(1, 2, 3), 6)
