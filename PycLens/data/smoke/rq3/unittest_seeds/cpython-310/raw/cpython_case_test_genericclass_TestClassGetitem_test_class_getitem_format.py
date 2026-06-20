# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __class_getitem__(cls, item):
            return f'C[{item.__name__}]'
    self.assertEqual(C[int], 'C[int]')
    self.assertEqual(C[C], 'C[C]')
