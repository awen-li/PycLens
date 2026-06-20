# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_annotated_refs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Const = Annotated[T, 'Const']

    class MySet(Generic[T]):

        def __ior__(self, other: 'Const[MySet[T]]') -> 'MySet[T]':
            ...

        def __iand__(self, other: Const['MySet[T]']) -> 'MySet[T]':
            ...
    self.assertEqual(get_type_hints(MySet.__iand__, globals(), locals()), {'other': MySet[T], 'return': MySet[T]})
    self.assertEqual(get_type_hints(MySet.__iand__, globals(), locals(), include_extras=True), {'other': Const[MySet[T]], 'return': MySet[T]})
    self.assertEqual(get_type_hints(MySet.__ior__, globals(), locals()), {'other': MySet[T], 'return': MySet[T]})
