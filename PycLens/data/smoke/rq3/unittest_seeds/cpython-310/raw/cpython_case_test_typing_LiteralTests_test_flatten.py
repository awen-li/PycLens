# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: LiteralTests_test_flatten

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l1 = Literal[Literal[1], Literal[2], Literal[3]]
    l2 = Literal[Literal[1, 2], 3]
    l3 = Literal[Literal[1, 2, 3]]
    for l in (l1, l2, l3):
        self.assertEqual(l, Literal[1, 2, 3])
        self.assertEqual(l.__args__, (1, 2, 3))
