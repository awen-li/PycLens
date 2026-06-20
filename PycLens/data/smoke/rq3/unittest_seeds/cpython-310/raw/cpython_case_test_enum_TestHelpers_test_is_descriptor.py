# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestHelpers_test_is_descriptor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class foo:
        pass
    for attr in ('__get__', '__set__', '__delete__'):
        obj = foo()
        self.assertFalse(enum._is_descriptor(obj))
        setattr(obj, attr, 1)
        self.assertTrue(enum._is_descriptor(obj))
