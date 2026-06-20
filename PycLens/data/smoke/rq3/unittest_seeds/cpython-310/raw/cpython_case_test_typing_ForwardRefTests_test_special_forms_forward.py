# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_special_forms_forward

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        a: Annotated['ClassVar[int]', (3, 5)] = 4
        b: Annotated['Final[int]', 'const'] = 4

    class CF:
        b: List['Final[int]'] = 4
    self.assertEqual(get_type_hints(C, globals())['a'], ClassVar[int])
    self.assertEqual(get_type_hints(C, globals())['b'], Final[int])
    with self.assertRaises(TypeError):
        (get_type_hints(CF, globals()),)
