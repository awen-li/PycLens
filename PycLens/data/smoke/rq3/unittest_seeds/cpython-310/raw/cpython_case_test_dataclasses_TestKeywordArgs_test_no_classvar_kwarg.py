# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestKeywordArgs_test_no_classvar_kwarg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'field a is a ClassVar but specifies kw_only'
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass
        class A:
            a: ClassVar[int] = field(kw_only=True)
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass
        class A:
            a: ClassVar[int] = field(kw_only=False)
    with self.assertRaisesRegex(TypeError, msg):

        @dataclass(kw_only=True)
        class A:
            a: ClassVar[int] = field(kw_only=False)
