# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem_inheritance_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __class_getitem__(cls, item):
            return 'Should not see this'

    class D(C):

        def __class_getitem__(cls, item):
            return f'{cls.__name__}[{item.__name__}]'
    self.assertEqual(D[int], 'D[int]')
    self.assertEqual(D[D], 'D[D]')
