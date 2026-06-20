# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_metaclass_dict_as_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        @property
        def __dict__(self):
            self.executed = True

    class Thing(metaclass=Meta):
        executed = False

        def __init__(self):
            self.spam = 42
    instance = Thing()
    self.assertEqual(inspect.getattr_static(instance, 'spam'), 42)
    self.assertFalse(Thing.executed)
