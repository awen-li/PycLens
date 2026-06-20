# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_nested_classvar_fails_forward_ref_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class E:
        foo: 'typing.ClassVar[typing.ClassVar[int]]' = 7

    class F:
        foo: ClassVar['ClassVar[int]'] = 7
    for clazz in [E, F]:
        with self.assertRaises(TypeError):
            get_type_hints(clazz)
