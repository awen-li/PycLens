# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_set_name_not_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cp = py_functools.cached_property(lambda s: None)

    class Foo:
        pass
    Foo.cp = cp
    with self.assertRaisesRegex(TypeError, 'Cannot use cached_property instance without calling __set_name__ on it.'):
        Foo().cp
