# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_forget

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod_filename = TESTFN + '.py'
    with open(mod_filename, 'w', encoding='utf-8') as f:
        print('foo = 1', file=f)
    sys.path.insert(0, os.curdir)
    importlib.invalidate_caches()
    try:
        mod = __import__(TESTFN)
        self.assertIn(TESTFN, sys.modules)
        import_helper.forget(TESTFN)
        self.assertNotIn(TESTFN, sys.modules)
    finally:
        del sys.path[0]
        os_helper.unlink(mod_filename)
        os_helper.rmtree('__pycache__')
