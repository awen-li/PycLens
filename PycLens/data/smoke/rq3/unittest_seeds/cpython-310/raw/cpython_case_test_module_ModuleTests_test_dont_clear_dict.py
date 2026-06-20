# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_dont_clear_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        foo = ModuleType('foo')
        foo.bar = 4
        return foo
    gc_collect()
    self.assertEqual(f().__dict__['bar'], 4)
