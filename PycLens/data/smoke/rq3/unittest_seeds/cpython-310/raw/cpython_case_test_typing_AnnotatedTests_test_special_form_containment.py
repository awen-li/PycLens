# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: AnnotatedTests_test_special_form_containment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        classvar: Annotated[ClassVar[int], 'a decoration'] = 4
        const: Annotated[Final[int], 'Const'] = 4
    self.assertEqual(get_type_hints(C, globals())['classvar'], ClassVar[int])
    self.assertEqual(get_type_hints(C, globals())['const'], Final[int])
