# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_reent_set_bases_on_direct_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(DebugHelperMeta):

        def mro(cls):
            base = cls.__bases__[0]
            if base is not object:
                if self.step_until(5):
                    base.__bases__ += ()
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B(A):
        pass

    class C(B):
        pass
