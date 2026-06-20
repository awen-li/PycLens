# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slots_multiple_inheritance

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(object):
        __slots__ = ()

    class B(object):
        pass

    class C(A, B):
        __slots__ = ()
    if support.check_impl_detail():
        self.assertEqual(C.__basicsize__, B.__basicsize__)
    self.assertHasAttr(C, '__dict__')
    self.assertHasAttr(C, '__weakref__')
    C().x = 2
