# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: CAPITest_test_c_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from _testcapi import Generic, GenericAlias
    self.assertIsInstance(Generic.__class_getitem__(int), GenericAlias)
    IntGeneric = Generic[int]
    self.assertIs(type(IntGeneric), GenericAlias)
    self.assertEqual(IntGeneric.__mro_entries__(()), (int,))

    class C(IntGeneric):
        pass
    self.assertEqual(C.__bases__, (int,))
    self.assertEqual(C.__orig_bases__, (IntGeneric,))
    self.assertEqual(C.__mro__, (C, int, object))
