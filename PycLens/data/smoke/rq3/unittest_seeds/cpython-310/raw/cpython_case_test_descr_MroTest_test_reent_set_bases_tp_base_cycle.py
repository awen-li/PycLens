# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_reent_set_bases_tp_base_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(DebugHelperMeta):

        def mro(cls):
            if self.ready:
                if cls.__name__ == 'B1':
                    B2.__bases__ = (B1,)
                if cls.__name__ == 'B2':
                    B1.__bases__ = (B2,)
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B1(A):
        pass

    class B2(A):
        pass
    self.ready = True
    with self.assertRaises(TypeError):
        B1.__bases__ += ()
