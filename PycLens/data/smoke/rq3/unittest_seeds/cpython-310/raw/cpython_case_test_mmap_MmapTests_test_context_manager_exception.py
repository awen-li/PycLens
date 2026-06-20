# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_context_manager_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(Exception) as exc:
        with mmap.mmap(-1, 10) as m:
            raise OSError
    self.assertIsInstance(exc.exception, OSError, 'wrong exception raised in context manager')
    self.assertTrue(m.closed, 'context manager failed')
