# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: SimpleNamespaceTests_test_fake_namespace_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class FakeSimpleNamespace(str):
        __class__ = types.SimpleNamespace
    self.assertFalse(types.SimpleNamespace() == FakeSimpleNamespace())
    self.assertTrue(types.SimpleNamespace() != FakeSimpleNamespace())
    with self.assertRaises(TypeError):
        types.SimpleNamespace() < FakeSimpleNamespace()
    with self.assertRaises(TypeError):
        types.SimpleNamespace() <= FakeSimpleNamespace()
    with self.assertRaises(TypeError):
        types.SimpleNamespace() > FakeSimpleNamespace()
    with self.assertRaises(TypeError):
        types.SimpleNamespace() >= FakeSimpleNamespace()
