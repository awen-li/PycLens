# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetUtilitiesTestCase_test_top_level_class_var

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'typing.ClassVar\\[int\\] is not valid as type argument'):
        get_type_hints(ann_module6)
