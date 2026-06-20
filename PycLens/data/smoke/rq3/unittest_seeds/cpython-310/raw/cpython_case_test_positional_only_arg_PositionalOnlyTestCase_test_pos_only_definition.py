# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_positional_only_arg.py
# case: PositionalOnlyTestCase_test_pos_only_definition

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f(a, b, c, /, d, e=1, *, f, g=2):
        pass
    self.assertEqual(5, f.__code__.co_argcount)
    self.assertEqual(3, f.__code__.co_posonlyargcount)
    self.assertEqual((1,), f.__defaults__)

    def f(a, b, c=1, /, d=2, e=3, *, f, g=4):
        pass
    self.assertEqual(5, f.__code__.co_argcount)
    self.assertEqual(3, f.__code__.co_posonlyargcount)
    self.assertEqual((1, 2, 3), f.__defaults__)
