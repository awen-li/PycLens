# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(hash(Literal[1]), hash(Literal[1]))
    self.assertEqual(hash(Literal[1, 2]), hash(Literal[2, 1]))
    self.assertEqual(hash(Literal[1, 2, 3]), hash(Literal[1, 2, 3, 3]))
