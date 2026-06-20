# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_no_runtime_deco_on_nominal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):

        @runtime_checkable
        class C:
            pass

    class Proto(Protocol):
        x = 1
    with self.assertRaises(TypeError):

        @runtime_checkable
        class Concrete(Proto):
            pass
