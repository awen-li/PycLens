# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_forward_equality_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c1 = typing.ForwardRef('int')
    c1_gth = typing.ForwardRef('int')
    c2 = typing.ForwardRef('int')
    c2_gth = typing.ForwardRef('int')

    def foo(a: c1_gth, b: c2_gth):
        pass
    get_type_hints(foo, globals(), locals())
    self.assertEqual(hash(c1), hash(c2))
    self.assertEqual(hash(c1_gth), hash(c2_gth))
    self.assertEqual(hash(c1), hash(c1_gth))
    c3 = typing.ForwardRef('int', module=__name__)
    c4 = typing.ForwardRef('int', module='__other_name__')
    self.assertNotEqual(hash(c3), hash(c1))
    self.assertNotEqual(hash(c3), hash(c1_gth))
    self.assertNotEqual(hash(c3), hash(c4))
    self.assertEqual(hash(c3), hash(typing.ForwardRef('int', module=__name__)))
