# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mimetypes.py
# case: Win32MimeTypesTestCase_test_registry_accelerator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from_accel = {}
    from_reg = {}
    _winapi._mimetypes_read_windows_registry(lambda v, k: from_accel.setdefault(k, set()).add(v))
    mimetypes.MimeTypes._read_windows_registry(lambda v, k: from_reg.setdefault(k, set()).add(v))
    self.assertEqual(list(from_reg), list(from_accel))
    for k in from_reg:
        self.assertEqual(from_reg[k], from_accel[k])
