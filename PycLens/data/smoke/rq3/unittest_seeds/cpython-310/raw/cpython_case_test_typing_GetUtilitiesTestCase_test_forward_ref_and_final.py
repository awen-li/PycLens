# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetUtilitiesTestCase_test_forward_ref_and_final

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hints = get_type_hints(ann_module5)
    self.assertEqual(hints, {'name': Final[str]})
    hints = get_type_hints(ann_module5.MyClass)
    self.assertEqual(hints, {'value': Final})
