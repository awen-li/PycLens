# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: TestPosixWeaklinking_test_pwritev

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._verify_available('HAVE_PWRITEV')
    if self.mac_ver >= (10, 16):
        self.assertTrue(hasattr(os, 'pwritev'), 'os.pwritev is not available')
        self.assertTrue(hasattr(os, 'preadv'), 'os.readv is not available')
    else:
        self.assertFalse(hasattr(os, 'pwritev'), 'os.pwritev is available')
        self.assertFalse(hasattr(os, 'preadv'), 'os.readv is available')
