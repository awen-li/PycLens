# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_ClassVar

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(gth(ann_module2.CV, ann_module2.__dict__), {'var': typing.ClassVar[ann_module2.CV]})
    self.assertEqual(gth(B, globals()), {'y': int, 'x': ClassVar[Optional[B]], 'b': int})
    self.assertEqual(gth(CSub, globals()), {'z': ClassVar[CSub], 'y': int, 'b': int, 'x': ClassVar[Optional[B]]})
    self.assertEqual(gth(G), {'lst': ClassVar[List[T]]})
