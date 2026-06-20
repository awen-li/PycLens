# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_contextmanager_attribs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    baz = self._create_contextmanager_attribs()
    self.assertEqual(baz.__name__, 'baz')
    self.assertEqual(baz.foo, 'bar')
