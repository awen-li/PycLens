# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem_errors_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __class_getitem__(cls, item):
            return None
    with self.assertRaises(TypeError):
        C()[int]

    class E:
        ...
    e = E()
    e.__class_getitem__ = lambda cls, item: 'This will not work'
    with self.assertRaises(TypeError):
        e[int]

    class C_not_callable:
        __class_getitem__ = 'Surprise!'
    with self.assertRaises(TypeError):
        C_not_callable[int]
