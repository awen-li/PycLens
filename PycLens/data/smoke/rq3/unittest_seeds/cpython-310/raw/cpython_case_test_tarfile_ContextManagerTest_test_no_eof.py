# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ContextManagerTest_test_no_eof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with tarfile.open(tmpname, 'w') as tar:
            raise Exception
    except:
        pass
    self.assertEqual(os.path.getsize(tmpname), 0, 'context manager wrote an end-of-archive block')
    self.assertTrue(tar.closed, 'context manager failed')
