# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_repr_with_bare_loader

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = ModuleType('foo')
    m.__loader__ = BareLoader
    module_repr = repr(BareLoader)
    self.assertEqual(repr(m), "<module 'foo' ({})>".format(module_repr))
