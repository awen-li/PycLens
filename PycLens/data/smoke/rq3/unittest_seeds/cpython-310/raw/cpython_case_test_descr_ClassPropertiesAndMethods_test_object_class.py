# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_object_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = object()
    self.assertEqual(a.__class__, object)
    self.assertEqual(type(a), object)
    b = object()
    self.assertNotEqual(a, b)
    self.assertNotHasAttr(a, 'foo')
    try:
        a.foo = 12
    except (AttributeError, TypeError):
        pass
    else:
        self.fail('object() should not allow setting a foo attribute')
    self.assertNotHasAttr(object(), '__dict__')

    class Cdict(object):
        pass
    x = Cdict()
    self.assertEqual(x.__dict__, {})
    x.foo = 1
    self.assertEqual(x.foo, 1)
    self.assertEqual(x.__dict__, {'foo': 1})
