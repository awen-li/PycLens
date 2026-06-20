# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property_builtin_doc_writable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = property(doc='basic')
    self.assertEqual(p.__doc__, 'basic')
    p.__doc__ = 'extended'
    self.assertEqual(p.__doc__, 'extended')
