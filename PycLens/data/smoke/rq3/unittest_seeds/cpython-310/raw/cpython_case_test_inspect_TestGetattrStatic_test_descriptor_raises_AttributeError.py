# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_descriptor_raises_AttributeError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class descriptor(object):

        def __get__(*_):
            raise AttributeError("I'm pretending not to exist")
    desc = descriptor()

    class Thing(object):
        x = desc
    thing = Thing()
    self.assertEqual(inspect.getattr_static(thing, 'x'), desc)
