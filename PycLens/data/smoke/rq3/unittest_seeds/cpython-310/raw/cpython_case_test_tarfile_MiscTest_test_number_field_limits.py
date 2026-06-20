# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: MiscTest_test_number_field_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        tarfile.itn(-1, 8, tarfile.USTAR_FORMAT)
    with self.assertRaises(ValueError):
        tarfile.itn(2097152, 8, tarfile.USTAR_FORMAT)
    with self.assertRaises(ValueError):
        tarfile.itn(-1099511627777, 6, tarfile.GNU_FORMAT)
    with self.assertRaises(ValueError):
        tarfile.itn(1099511627776, 6, tarfile.GNU_FORMAT)
