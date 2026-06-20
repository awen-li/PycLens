# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_equal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotEqual(Literal[0], Literal[False])
    self.assertNotEqual(Literal[True], Literal[1])
    self.assertNotEqual(Literal[1], Literal[2])
    self.assertNotEqual(Literal[1, True], Literal[1])
    self.assertNotEqual(Literal[1, True], Literal[1, 1])
    self.assertNotEqual(Literal[1, 2], Literal[True, 2])
    self.assertEqual(Literal[1], Literal[1])
    self.assertEqual(Literal[1, 2], Literal[2, 1])
    self.assertEqual(Literal[1, 2, 3], Literal[1, 2, 3, 3])
