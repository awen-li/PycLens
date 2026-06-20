# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Thing(object):
        y = 'bar'
        __slots__ = ['x']

        def __init__(self):
            self.x = 'foo'
    thing = Thing()
    self.assertEqual(inspect.getattr_static(thing, 'x'), Thing.x)
    self.assertEqual(inspect.getattr_static(thing, 'y'), 'bar')
    del thing.x
    self.assertEqual(inspect.getattr_static(thing, 'x'), Thing.x)
