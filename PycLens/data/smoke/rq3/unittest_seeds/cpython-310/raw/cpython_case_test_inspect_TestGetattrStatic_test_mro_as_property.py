# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_mro_as_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        @property
        def __mro__(self):
            return (object,)

    class Base(object):
        foo = 3

    class Something(Base, metaclass=Meta):
        pass
    self.assertEqual(inspect.getattr_static(Something(), 'foo'), 3)
    self.assertEqual(inspect.getattr_static(Something, 'foo'), 3)
