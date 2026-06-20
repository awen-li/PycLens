# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ContextManagerTest_test_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with tarfile.open(tmpname, 'w'):
        pass
    self.assertNotEqual(os.path.getsize(tmpname), 0, 'context manager wrote no end-of-archive block')
