# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_new_class_meta_with_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Meta = self.Meta

    def func(ns):
        ns['x'] = 0
    C = types.new_class(name='C', bases=(int,), kwds=dict(metaclass=Meta, z=2), exec_body=func)
    self.assertTrue(issubclass(C, int))
    self.assertIsInstance(C, Meta)
    self.assertEqual(C.x, 0)
    self.assertEqual(C.y, 1)
    self.assertEqual(C.z, 2)
