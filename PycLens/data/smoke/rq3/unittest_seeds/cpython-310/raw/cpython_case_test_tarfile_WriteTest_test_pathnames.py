# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: WriteTest_test_pathnames

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._test_pathname('foo')
    self._test_pathname(os.path.join('foo', '.', 'bar'))
    self._test_pathname(os.path.join('foo', '..', 'bar'))
    self._test_pathname(os.path.join('.', 'foo'))
    self._test_pathname(os.path.join('.', 'foo', '.'))
    self._test_pathname(os.path.join('.', 'foo', '.', 'bar'))
    self._test_pathname(os.path.join('.', 'foo', '..', 'bar'))
    self._test_pathname(os.path.join('.', 'foo', '..', 'bar'))
    self._test_pathname(os.path.join('..', 'foo'))
    self._test_pathname(os.path.join('..', 'foo', '..'))
    self._test_pathname(os.path.join('..', 'foo', '.', 'bar'))
    self._test_pathname(os.path.join('..', 'foo', '..', 'bar'))
    self._test_pathname('foo' + os.sep + os.sep + 'bar')
    self._test_pathname('foo' + os.sep + os.sep, 'foo', dir=True)
