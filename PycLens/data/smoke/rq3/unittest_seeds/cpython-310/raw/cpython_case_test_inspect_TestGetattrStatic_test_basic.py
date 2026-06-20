# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Thing(object):
        x = object()
    thing = Thing()
    self.assertEqual(inspect.getattr_static(thing, 'x'), Thing.x)
    self.assertEqual(inspect.getattr_static(thing, 'x', None), Thing.x)
    with self.assertRaises(AttributeError):
        inspect.getattr_static(thing, 'y')
    self.assertEqual(inspect.getattr_static(thing, 'y', 3), 3)
