# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericpath.py
# case: CommonTest_test_abspath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('foo', self.pathmodule.abspath('foo'))
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        self.assertIn(b'foo', self.pathmodule.abspath(b'foo'))
    undecodable_path = b'' if sys.platform == 'win32' else b'f\xf2\xf2'
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        for path in (b'', b'foo', undecodable_path, b'/foo', b'C:\\'):
            self.assertIsInstance(self.pathmodule.abspath(path), bytes)
