# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LimitsTest_test_ustar_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = tarfile.TarInfo('0123456789' * 10)
    tarinfo.tobuf(tarfile.USTAR_FORMAT)
    tarinfo = tarfile.TarInfo('0123456789' * 10 + '0')
    self.assertRaises(ValueError, tarinfo.tobuf, tarfile.USTAR_FORMAT)
    tarinfo = tarfile.TarInfo('123/' * 62 + 'longname')
    tarinfo.tobuf(tarfile.USTAR_FORMAT)
    tarinfo = tarfile.TarInfo('1234567/' * 31 + 'longname')
    self.assertRaises(ValueError, tarinfo.tobuf, tarfile.USTAR_FORMAT)
    tarinfo = tarfile.TarInfo('123/' * 126 + 'longname')
    self.assertRaises(ValueError, tarinfo.tobuf, tarfile.USTAR_FORMAT)
    tarinfo = tarfile.TarInfo('longlink')
    tarinfo.linkname = '123/' * 126 + 'longname'
    self.assertRaises(ValueError, tarinfo.tobuf, tarfile.USTAR_FORMAT)
    tarinfo = tarfile.TarInfo('name')
    tarinfo.uid = 2097152
    self.assertRaises(ValueError, tarinfo.tobuf, tarfile.USTAR_FORMAT)
