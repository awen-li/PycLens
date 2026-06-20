# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_forward_equality_gth

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c1 = typing.ForwardRef('C')
    c1_gth = typing.ForwardRef('C')
    c2 = typing.ForwardRef('C')
    c2_gth = typing.ForwardRef('C')

    class C:
        pass

    def foo(a: c1_gth, b: c2_gth):
        pass
    self.assertEqual(get_type_hints(foo, globals(), locals()), {'a': C, 'b': C})
    self.assertEqual(c1, c2)
    self.assertEqual(c1, c1_gth)
    self.assertEqual(c1_gth, c2_gth)
    self.assertEqual(List[c1], List[c1_gth])
    self.assertNotEqual(List[c1], List[C])
    self.assertNotEqual(List[c1_gth], List[C])
    self.assertEqual(Union[c1, c1_gth], Union[c1])
    self.assertEqual(Union[c1, c1_gth, int], Union[c1, int])
