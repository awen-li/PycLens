# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_reent_set_bases_on_base

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(DebugHelperMeta):

        def mro(cls):
            if cls.__mro__ is not None and cls.__name__ == 'B':
                if self.step_until(10):
                    A.__bases__ += ()
            return type.mro(cls)

    class A(metaclass=M):
        pass

    class B(A):
        pass
    B.__bases__ += ()
