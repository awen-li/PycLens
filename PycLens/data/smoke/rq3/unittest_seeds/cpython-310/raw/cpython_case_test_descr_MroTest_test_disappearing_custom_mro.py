# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_disappearing_custom_mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class B:
        pass

    class M(DebugHelperMeta):

        def mro(cls):
            del M.mro
            return (B,)
    with self.assertRaises(TypeError):

        class A(metaclass=M):
            pass
