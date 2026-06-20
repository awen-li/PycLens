# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_incomplete_set_bases_on_self

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(DebugHelperMeta):

        def mro(cls):
            if self.step_until(1):
                assert cls.__mro__ is None
                cls.__bases__ += ()
            return type.mro(cls)

    class A(metaclass=M):
        pass
