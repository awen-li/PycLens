# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @dataclass
    class A:
        a: int = 0
        _: KW_ONLY
        b: int
        c: int = 1
        d: int
    a = A(d=4, b=3)
    self.assertEqual(a.a, 0)
    self.assertEqual(a.b, 3)
    self.assertEqual(a.c, 1)
    self.assertEqual(a.d, 4)
    err_regex = "non-default argument 'z' follows default argument"
    with self.assertRaisesRegex(TypeError, err_regex):

        @dataclass
        class A:
            a: int = 0
            z: int
            _: KW_ONLY
            b: int
            c: int = 1
            d: int
