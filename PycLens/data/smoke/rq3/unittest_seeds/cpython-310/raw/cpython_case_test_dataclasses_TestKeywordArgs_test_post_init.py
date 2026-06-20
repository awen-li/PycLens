# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_post_init

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class A:
        a: int
        _: KW_ONLY
        b: InitVar[int]
        c: int
        d: InitVar[int]

        def __post_init__(self, b, d):
            raise CustomError(f'b={b!r} d={d!r}')
    with self.assertRaisesRegex(CustomError, 'b=3 d=4'):
        A(1, c=2, b=3, d=4)

    @dataclass
    class B:
        a: int
        _: KW_ONLY
        b: InitVar[int]
        c: int
        d: InitVar[int]

        def __post_init__(self, b, d):
            self.a = b
            self.c = d
    b = B(1, c=2, b=3, d=4)
    self.assertEqual(asdict(b), {'a': 3, 'c': 4})
