# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_bundled_protocol_instance_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(0, typing.SupportsAbs)

    class C1(typing.SupportsInt):

        def __int__(self) -> int:
            return 42

    class C2(C1):
        pass
    c = C2()
    self.assertIsInstance(c, C1)
