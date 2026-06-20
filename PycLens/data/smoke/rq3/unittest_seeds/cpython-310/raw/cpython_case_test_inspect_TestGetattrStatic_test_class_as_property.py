# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_class_as_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base(object):
        foo = 3

    class Something(Base):
        executed = False

        @property
        def __class__(self):
            self.executed = True
            return object
    instance = Something()
    self.assertEqual(inspect.getattr_static(instance, 'foo'), 3)
    self.assertFalse(instance.executed)
    self.assertEqual(inspect.getattr_static(Something, 'foo'), 3)
