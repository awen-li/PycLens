# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_subclass_special_form

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for obj in (ClassVar[int], Final[int], Union[int, float], Optional[int], Literal[1, 2], Concatenate[int, ParamSpec('P')], TypeGuard[int]):
        with self.subTest(msg=obj):
            with self.assertRaisesRegex(TypeError, f"^{re.escape(f'Cannot subclass {obj!r}')}$"):

                class Foo(obj):
                    pass
