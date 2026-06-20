# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_no_type_check_forward_ref_as_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:
        foo: typing.ClassVar[int] = 7

    class D:
        foo: ClassVar[int] = 7

    class E:
        foo: 'typing.ClassVar[int]' = 7

    class F:
        foo: 'ClassVar[int]' = 7
    expected_result = {'foo': typing.ClassVar[int]}
    for clazz in [C, D, E, F]:
        self.assertEqual(get_type_hints(clazz), expected_result)
