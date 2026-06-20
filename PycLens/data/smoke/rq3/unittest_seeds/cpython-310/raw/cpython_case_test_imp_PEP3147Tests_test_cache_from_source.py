# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imp.py
# case: PEP3147Tests_test_cache_from_source

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join('foo', 'bar', 'baz', 'qux.py')
    expect = os.path.join('foo', 'bar', 'baz', '__pycache__', 'qux.{}.pyc'.format(self.tag))
    self.assertEqual(imp.cache_from_source(path, True), expect)
