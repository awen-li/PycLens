# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_annotations_getset_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    foo = ModuleType.__new__(ModuleType)
    with self.assertRaises(TypeError):
        print(foo.__annotations__)
    with self.assertRaises(TypeError):
        foo.__annotations__ = {}
    with self.assertRaises(TypeError):
        del foo.__annotations__
    foo = ModuleType('foo')
    foo.__annotations__ = {}
    del foo.__annotations__
    with self.assertRaises(AttributeError):
        del foo.__annotations__
