# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_KW_ONLY_twice

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = "'Y' is KW_ONLY, but KW_ONLY has already been specified"
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass
        class A:
            a: int
            X: KW_ONLY
            Y: KW_ONLY
            b: int
            c: int
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass
        class A:
            a: int
            X: KW_ONLY
            b: int
            Y: KW_ONLY
            c: int
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass
        class A:
            a: int
            X: KW_ONLY
            b: int
            c: int
            Y: KW_ONLY

    @dataclass
    class A:
        a: int
        _: KW_ONLY
        b: int
        c: int = field(kw_only=True)

    @dataclass
    class A:
        a: int
        _: KW_ONLY
        b: int
        c: int

    @dataclass
    class B(A):
        _: KW_ONLY
        d: int
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass
        class A:
            a: int
            _: KW_ONLY
            b: int
            c: int

        @dataclass
        class B(A):
            X: KW_ONLY
            d: int
            Y: KW_ONLY
