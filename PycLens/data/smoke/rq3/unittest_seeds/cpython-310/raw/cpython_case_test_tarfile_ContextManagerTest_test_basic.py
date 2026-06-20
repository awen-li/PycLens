# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ContextManagerTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tarname) as tar:
        self.assertFalse(tar.closed, 'closed inside runtime context')
    self.assertTrue(tar.closed, 'context manager failed')
