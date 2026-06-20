# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_tuple_forward

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a: Tuple['T']):
        pass
    self.assertEqual(get_type_hints(foo, globals(), locals()), {'a': Tuple[T]})

    def foo(a: tuple[ForwardRef('T')]):
        pass
    self.assertEqual(get_type_hints(foo, globals(), locals()), {'a': tuple[T]})
