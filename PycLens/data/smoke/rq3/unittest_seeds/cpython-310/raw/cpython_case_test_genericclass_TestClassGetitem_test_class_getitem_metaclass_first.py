# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem_metaclass_first

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __getitem__(cls, item):
            return 'from metaclass'

    class C(metaclass=Meta):

        def __class_getitem__(cls, item):
            return 'from __class_getitem__'
    self.assertEqual(C[int], 'from metaclass')
