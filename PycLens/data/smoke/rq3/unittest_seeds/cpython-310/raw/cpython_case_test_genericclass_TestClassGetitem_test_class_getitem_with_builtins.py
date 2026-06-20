# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestClassGetitem_test_class_getitem_with_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(dict):
        called_with = None

        def __class_getitem__(cls, item):
            cls.called_with = item

    class B(A):
        pass
    self.assertIs(B.called_with, None)
    B[int]
    self.assertIs(B.called_with, int)
