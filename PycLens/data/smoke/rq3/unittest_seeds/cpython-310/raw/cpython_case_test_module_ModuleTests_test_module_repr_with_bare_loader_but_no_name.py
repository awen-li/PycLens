# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_module_repr_with_bare_loader_but_no_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = ModuleType('foo')
    del m.__name__
    m.__loader__ = BareLoader
    loader_repr = repr(BareLoader)
    self.assertEqual(repr(m), "<module '?' ({})>".format(loader_repr))
