# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_tp_subclasses_cycle_in_update_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(DebugHelperMeta):

        def mro(cls):
            if self.ready and cls.__name__ == 'C':
                self.ready = False
                C.__bases__ = (B2,)
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B1(A):
        pass

    class B2(A):
        pass

    class C(A):
        pass
    self.ready = True
    C.__bases__ = (B1,)
    B1.__bases__ = (C,)
    self.assertEqual(C.__bases__, (B2,))
    self.assertEqual(B2.__subclasses__(), [C])
    self.assertEqual(B1.__subclasses__(), [])
    self.assertEqual(B1.__bases__, (C,))
    self.assertEqual(C.__subclasses__(), [B1])
