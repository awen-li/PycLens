# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_abc_registry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = dict(a=1)
    self.assertIsInstance(d.keys(), collections.abc.KeysView)
    self.assertIsInstance(d.keys(), collections.abc.MappingView)
    self.assertIsInstance(d.keys(), collections.abc.Set)
    self.assertIsInstance(d.keys(), collections.abc.Sized)
    self.assertIsInstance(d.keys(), collections.abc.Iterable)
    self.assertIsInstance(d.keys(), collections.abc.Container)
    self.assertIsInstance(d.values(), collections.abc.ValuesView)
    self.assertIsInstance(d.values(), collections.abc.MappingView)
    self.assertIsInstance(d.values(), collections.abc.Sized)
    self.assertIsInstance(d.values(), collections.abc.Collection)
    self.assertIsInstance(d.values(), collections.abc.Iterable)
    self.assertIsInstance(d.values(), collections.abc.Container)
    self.assertIsInstance(d.items(), collections.abc.ItemsView)
    self.assertIsInstance(d.items(), collections.abc.MappingView)
    self.assertIsInstance(d.items(), collections.abc.Set)
    self.assertIsInstance(d.items(), collections.abc.Sized)
    self.assertIsInstance(d.items(), collections.abc.Iterable)
    self.assertIsInstance(d.items(), collections.abc.Container)
