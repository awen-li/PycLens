# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: ImportTests_test_issue16421_multiple_modules_in_one_dll

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = '_testimportmultiple'
    (fileobj, pathname, description) = imp.find_module(m)
    fileobj.close()
    mod0 = imp.load_dynamic(m, pathname)
    mod1 = imp.load_dynamic('_testimportmultiple_foo', pathname)
    mod2 = imp.load_dynamic('_testimportmultiple_bar', pathname)
    self.assertEqual(mod0.__name__, m)
    self.assertEqual(mod1.__name__, '_testimportmultiple_foo')
    self.assertEqual(mod2.__name__, '_testimportmultiple_bar')
    with self.assertRaises(ImportError):
        imp.load_dynamic('nonexistent', pathname)
