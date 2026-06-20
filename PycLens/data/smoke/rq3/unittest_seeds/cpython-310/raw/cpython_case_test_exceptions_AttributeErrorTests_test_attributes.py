# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: AttributeErrorTests_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    exc = AttributeError('Ouch!')
    self.assertIsNone(exc.name)
    self.assertIsNone(exc.obj)
    sentinel = object()
    exc = AttributeError('Ouch', name='carry', obj=sentinel)
    self.assertEqual(exc.name, 'carry')
    self.assertIs(exc.obj, sentinel)
