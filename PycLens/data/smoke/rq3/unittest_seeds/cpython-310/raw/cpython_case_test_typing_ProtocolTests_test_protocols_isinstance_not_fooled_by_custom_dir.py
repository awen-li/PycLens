# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_protocols_isinstance_not_fooled_by_custom_dir

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @runtime_checkable
    class HasX(Protocol):
        x: int

    class CustomDirWithX:
        x = 10

        def __dir__(self):
            return []

    class CustomDirWithoutX:

        def __dir__(self):
            return ['x']
    self.assertIsInstance(CustomDirWithX(), HasX)
    self.assertNotIsInstance(CustomDirWithoutX(), HasX)
