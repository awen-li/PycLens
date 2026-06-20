# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_module.py
# case: ModuleTests_test_descriptor_errors_propagate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descr:

        def __get__(self, o, t):
            raise RuntimeError

    class M(ModuleType):
        melon = Descr()
    self.assertRaises(RuntimeError, getattr, M('mymod'), 'melon')
