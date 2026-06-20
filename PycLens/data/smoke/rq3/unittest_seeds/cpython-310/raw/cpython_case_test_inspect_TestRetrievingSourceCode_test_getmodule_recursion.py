# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getmodule_recursion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from types import ModuleType
    name = '__inspect_dummy'
    m = sys.modules[name] = ModuleType(name)
    m.__file__ = '<string>'
    m.__loader__ = 'dummy'
    exec('def x(): pass', m.__dict__)
    self.assertEqual(inspect.getsourcefile(m.x.__code__), '<string>')
    del sys.modules[name]
    inspect.getmodule(compile('a=10', '', 'single'))
