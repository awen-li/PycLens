# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: FinalTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Final[int]
    with self.assertRaises(TypeError):
        Final[1]
    with self.assertRaises(TypeError):
        Final[int, str]
    with self.assertRaises(TypeError):
        Final[int][str]
    with self.assertRaises(TypeError):
        Optional[Final[int]]
