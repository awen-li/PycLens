# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ContextManagerTest_test_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tarname)
    tar.close()
    with self.assertRaises(OSError):
        with tar:
            pass
