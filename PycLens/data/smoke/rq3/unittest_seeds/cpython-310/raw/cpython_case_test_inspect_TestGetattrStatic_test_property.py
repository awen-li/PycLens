# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Thing(object):

        @property
        def x(self):
            raise AttributeError("I'm pretending not to exist")
    thing = Thing()
    self.assertEqual(inspect.getattr_static(thing, 'x'), Thing.x)
