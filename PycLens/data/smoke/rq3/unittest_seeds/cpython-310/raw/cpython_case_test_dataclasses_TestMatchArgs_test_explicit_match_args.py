# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestMatchArgs_test_explicit_match_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ma = ()

    @dataclass
    class C:
        a: int
        __match_args__ = ma
    self.assertIs(C(42).__match_args__, ma)
