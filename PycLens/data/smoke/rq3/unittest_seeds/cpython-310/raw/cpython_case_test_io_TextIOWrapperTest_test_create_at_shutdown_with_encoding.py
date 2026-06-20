# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_create_at_shutdown_with_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rc, out, err) = self._check_create_at_shutdown(encoding='utf-8', errors='strict')
    self.assertFalse(err)
    self.assertEqual('ok', out.decode().strip())
