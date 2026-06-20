# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_modules

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ann_module_type_hints = {1: 2, 'f': Tuple[int, int], 'x': int, 'y': str, 'u': int | float}
    self.assertEqual(gth(ann_module), ann_module_type_hints)
    self.assertEqual(gth(ann_module2), {})
    self.assertEqual(gth(ann_module3), {})
