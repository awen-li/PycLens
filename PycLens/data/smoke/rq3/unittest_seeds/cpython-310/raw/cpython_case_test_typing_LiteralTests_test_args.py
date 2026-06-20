# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Literal[1, 2, 3].__args__, (1, 2, 3))
    self.assertEqual(Literal[1, 2, 3, 3].__args__, (1, 2, 3))
    self.assertEqual(Literal[1, Literal[2], Literal[3, 4]].__args__, (1, 2, 3, 4))
    self.assertEqual(Literal[[], []].__args__, ([], []))
