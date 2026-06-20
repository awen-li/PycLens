# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_make_dataclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = make_dataclass('A', ['a'], kw_only=True)
    self.assertTrue(fields(A)[0].kw_only)
    B = make_dataclass('B', ['a', ('b', int, field(kw_only=False))], kw_only=True)
    self.assertTrue(fields(B)[0].kw_only)
    self.assertFalse(fields(B)[1].kw_only)
