# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_union_forward_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ValueList = List['Value']
    Value = Union[str, ValueList]

    class C:
        foo: List[Value]

    class D:
        foo: Union[Value, ValueList]

    class E:
        foo: Union[List[Value], ValueList]

    class F:
        foo: Union[Value, List[Value], ValueList]
    self.assertEqual(get_type_hints(C, globals(), locals()), get_type_hints(C, globals(), locals()))
    self.assertEqual(get_type_hints(C, globals(), locals()), {'foo': List[Union[str, List[Union[str, List['Value']]]]]})
    self.assertEqual(get_type_hints(D, globals(), locals()), {'foo': Union[str, List[Union[str, List['Value']]]]})
    self.assertEqual(get_type_hints(E, globals(), locals()), {'foo': Union[List[Union[str, List[Union[str, List['Value']]]]], List[Union[str, List['Value']]]]})
    self.assertEqual(get_type_hints(F, globals(), locals()), {'foo': Union[str, List[Union[str, List['Value']]], List[Union[str, List[Union[str, List['Value']]]]]]})
