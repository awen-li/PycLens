# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pkgutil.py
# case: PkgutilPEP302Tests_test_alreadyloaded

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import foo
    self.assertEqual(foo.loads, 1)
    self.assertEqual(pkgutil.get_data('foo', 'dummy'), 'Hello, world!')
    self.assertEqual(foo.loads, 1)
    del sys.modules['foo']
