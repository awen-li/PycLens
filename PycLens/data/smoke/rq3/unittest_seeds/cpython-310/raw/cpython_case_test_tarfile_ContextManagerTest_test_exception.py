# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ContextManagerTest_test_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(Exception) as exc:
        with tarfile.open(tarname) as tar:
            raise OSError
    self.assertIsInstance(exc.exception, OSError, 'wrong exception raised in context manager')
    self.assertTrue(tar.closed, 'context manager failed')
