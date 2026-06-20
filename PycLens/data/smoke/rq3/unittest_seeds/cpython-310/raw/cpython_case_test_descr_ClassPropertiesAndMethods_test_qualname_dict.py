# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_qualname_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {'__qualname__': 'some.name'}
    tp = type('Foo', (), ns)
    self.assertEqual(tp.__qualname__, 'some.name')
    self.assertNotIn('__qualname__', tp.__dict__)
    self.assertEqual(ns, {'__qualname__': 'some.name'})
    ns = {'__qualname__': 1}
    self.assertRaises(TypeError, type, 'Foo', (), ns)
