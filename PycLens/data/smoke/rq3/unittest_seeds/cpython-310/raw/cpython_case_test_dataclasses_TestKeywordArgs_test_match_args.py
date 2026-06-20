# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_match_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(kw_only=True)
    class C:
        a: int
    self.assertEqual(C(a=42).__match_args__, ())

    @dataclass
    class C:
        a: int
        b: int = field(kw_only=True)
    self.assertEqual(C(42, b=10).__match_args__, ('a',))
