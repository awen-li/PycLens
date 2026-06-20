# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C_too_few:

        def __class_getitem__(cls):
            return None
    with self.assertRaises(TypeError):
        C_too_few[int]

    class C_too_many:

        def __class_getitem__(cls, one, two):
            return None
    with self.assertRaises(TypeError):
        C_too_many[int]
