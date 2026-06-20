# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_instance_attr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Thing(object):
        x = 2

        def __init__(self, x):
            self.x = x
    thing = Thing(3)
    self.assertEqual(inspect.getattr_static(thing, 'x'), 3)
    del thing.x
    self.assertEqual(inspect.getattr_static(thing, 'x'), 2)
