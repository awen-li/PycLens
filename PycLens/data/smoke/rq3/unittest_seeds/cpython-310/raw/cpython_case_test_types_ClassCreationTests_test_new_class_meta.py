# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_new_class_meta

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Meta = self.Meta
    settings = {'metaclass': Meta, 'z': 2}
    for i in range(2):
        C = types.new_class('C' + str(i), (), settings)
        self.assertIsInstance(C, Meta)
        self.assertEqual(C.y, 1)
        self.assertEqual(C.z, 2)
