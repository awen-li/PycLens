# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_metaclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class meta(type):
        attr = 'foo'

    class Thing(object, metaclass=meta):
        pass
    self.assertEqual(inspect.getattr_static(Thing, 'attr'), 'foo')

    class sub(meta):
        pass

    class OtherThing(object, metaclass=sub):
        x = 3
    self.assertEqual(inspect.getattr_static(OtherThing, 'attr'), 'foo')

    class OtherOtherThing(OtherThing):
        pass
    self.assertEqual(inspect.getattr_static(OtherOtherThing, 'x'), 3)
