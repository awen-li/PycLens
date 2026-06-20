# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_KW_ONLY

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class A:
        a: int
        _: KW_ONLY
        b: int
        c: int
    A(3, c=5, b=4)
    msg = 'takes 2 positional arguments but 4 were given'
    with self.assertRaisesRegex(TypeError, msg):
        A(3, 4, 5)

    @dataclass(kw_only=True)
    class B:
        a: int
        _: KW_ONLY
        b: int
        c: int
    B(a=3, b=4, c=5)
    msg = 'takes 1 positional argument but 4 were given'
    with self.assertRaisesRegex(TypeError, msg):
        B(3, 4, 5)

    @dataclass
    class C:
        a: int
        _: KW_ONLY
        b: int
        c: int = field(kw_only=False)
    c = C(1, 2, b=3)
    self.assertEqual(c.a, 1)
    self.assertEqual(c.b, 3)
    self.assertEqual(c.c, 2)
    c = C(1, b=3, c=2)
    self.assertEqual(c.a, 1)
    self.assertEqual(c.b, 3)
    self.assertEqual(c.c, 2)
    c = C(1, b=3, c=2)
    self.assertEqual(c.a, 1)
    self.assertEqual(c.b, 3)
    self.assertEqual(c.c, 2)
    c = C(c=2, b=3, a=1)
    self.assertEqual(c.a, 1)
    self.assertEqual(c.b, 3)
    self.assertEqual(c.c, 2)
