# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_field_marked_as_kwonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass(kw_only=True)
    class A:
        a: int
    self.assertTrue(fields(A)[0].kw_only)

    @dataclass(kw_only=True)
    class A:
        a: int = field(kw_only=True)
    self.assertTrue(fields(A)[0].kw_only)

    @dataclass(kw_only=True)
    class A:
        a: int = field(kw_only=False)
    self.assertFalse(fields(A)[0].kw_only)

    @dataclass(kw_only=False)
    class A:
        a: int
    self.assertFalse(fields(A)[0].kw_only)

    @dataclass(kw_only=False)
    class A:
        a: int = field(kw_only=True)
    self.assertTrue(fields(A)[0].kw_only)

    @dataclass(kw_only=False)
    class A:
        a: int = field(kw_only=False)
    self.assertFalse(fields(A)[0].kw_only)

    @dataclass
    class A:
        a: int
    self.assertFalse(fields(A)[0].kw_only)

    @dataclass
    class A:
        a: int = field(kw_only=True)
    self.assertTrue(fields(A)[0].kw_only)

    @dataclass
    class A:
        a: int = field(kw_only=False)
    self.assertFalse(fields(A)[0].kw_only)
