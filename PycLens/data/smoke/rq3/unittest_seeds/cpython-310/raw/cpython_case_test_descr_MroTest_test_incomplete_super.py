# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: MroTest_test_incomplete_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class M(DebugHelperMeta):

        def mro(cls):
            if cls.__mro__ is None:
                with self.assertRaises(AttributeError):
                    super(cls, cls).xxx
            return type.mro(cls)

    class A(metaclass=M):
        pass
