# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_classes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(gth(ann_module.C), {'y': Optional[ann_module.C]})
    self.assertIsInstance(gth(ann_module.j_class), dict)
    self.assertEqual(gth(ann_module.M), {'123': 123, 'o': type})
    self.assertEqual(gth(ann_module.D), {'j': str, 'k': str, 'y': Optional[ann_module.C]})
    self.assertEqual(gth(ann_module.Y), {'z': int})
    self.assertEqual(gth(ann_module.h_class), {'y': Optional[ann_module.C]})
    self.assertEqual(gth(ann_module.S), {'x': str, 'y': str})
    self.assertEqual(gth(ann_module.foo), {'x': int})
    self.assertEqual(gth(NoneAndForward), {'parent': NoneAndForward, 'meaning': type(None)})
    self.assertEqual(gth(HasForeignBaseClass), {'some_xrepr': XRepr, 'other_a': mod_generics_cache.A, 'some_b': mod_generics_cache.B})
    self.assertEqual(gth(XRepr.__new__), {'x': int, 'y': int})
    self.assertEqual(gth(mod_generics_cache.B), {'my_inner_a1': mod_generics_cache.B.A, 'my_inner_a2': mod_generics_cache.B.A, 'my_outer_a': mod_generics_cache.A})
