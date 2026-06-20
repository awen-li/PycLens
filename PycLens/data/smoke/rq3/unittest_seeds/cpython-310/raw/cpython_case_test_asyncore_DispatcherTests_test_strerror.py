# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: DispatcherTests_test_strerror

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    err = asyncore._strerror(errno.EPERM)
    if hasattr(os, 'strerror'):
        self.assertEqual(err, os.strerror(errno.EPERM))
    err = asyncore._strerror(-1)
    self.assertTrue(err != '')
