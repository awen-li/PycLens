# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_metaclass_with_metaclass_with_dict_as_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MetaMeta(type):

        @property
        def __dict__(self):
            self.executed = True
            return dict(spam=42)

    class Meta(type, metaclass=MetaMeta):
        executed = False

    class Thing(metaclass=Meta):
        pass
    with self.assertRaises(AttributeError):
        inspect.getattr_static(Thing, 'spam')
    self.assertFalse(Thing.executed)
