# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_with_genericalias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = list[int]
    b = list[str]
    c = dict[float, str]

    class SubClass(types.GenericAlias):
        ...
    d = SubClass(list, float)
    self.assertEqual(a | b | c | d, typing.Union[a, b, c, d])
    self.assertEqual(a | c | b | b | a | c | d | d, a | b | c | d)
    self.assertEqual(a | b | d, b | a | d)
    self.assertEqual(repr(a | b | c | d), 'list[int] | list[str] | dict[float, str] | list[float]')

    class BadType(type):

        def __eq__(self, other):
            return 1 / 0
    bt = BadType('bt', (), {})
    with self.assertRaises(ZeroDivisionError):
        list[int] | list[bt]
    union_ga = (int | list[str], int | collections.abc.Callable[..., str], int | d)
    for type_ in union_ga:
        with self.subTest(f'check isinstance/issubclass is invalid for {type_}'):
            with self.assertRaises(TypeError):
                isinstance(1, type_)
            with self.assertRaises(TypeError):
                issubclass(int, type_)
