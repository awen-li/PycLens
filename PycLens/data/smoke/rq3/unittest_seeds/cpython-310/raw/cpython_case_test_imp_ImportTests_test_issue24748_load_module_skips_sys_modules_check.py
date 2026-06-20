# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue24748_load_module_skips_sys_modules_check

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    name = 'test.imp_dummy'
    try:
        del sys.modules[name]
    except KeyError:
        pass
    try:
        module = importlib.import_module(name)
        spec = importlib.util.find_spec('_testmultiphase')
        module = imp.load_dynamic(name, spec.origin)
        self.assertEqual(module.__name__, name)
        self.assertEqual(module.__spec__.name, name)
        self.assertEqual(module.__spec__.origin, spec.origin)
        self.assertRaises(AttributeError, getattr, module, 'dummy_name')
        self.assertEqual(module.int_const, 1969)
        self.assertIs(sys.modules[name], module)
    finally:
        try:
            del sys.modules[name]
        except KeyError:
            pass
