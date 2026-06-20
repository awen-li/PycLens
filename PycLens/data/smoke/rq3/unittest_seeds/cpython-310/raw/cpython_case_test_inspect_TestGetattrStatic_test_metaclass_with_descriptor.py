# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_metaclass_with_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class descriptor(object):

        def __get__(self, instance, owner):
            return 3

    class meta(type):
        d = descriptor()

    class Thing(object, metaclass=meta):
        pass
    self.assertEqual(inspect.getattr_static(Thing, 'd'), meta.__dict__['d'])
