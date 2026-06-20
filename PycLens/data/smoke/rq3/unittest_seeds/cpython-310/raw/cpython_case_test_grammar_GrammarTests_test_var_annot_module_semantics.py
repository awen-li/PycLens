# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_module_semantics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(test.__annotations__, {})
    self.assertEqual(ann_module.__annotations__, {1: 2, 'x': int, 'y': str, 'f': typing.Tuple[int, int], 'u': int | float})
    self.assertEqual(ann_module.M.__annotations__, {'123': 123, 'o': type})
    self.assertEqual(ann_module2.__annotations__, {})
