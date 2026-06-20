# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LimitsTest_test_gnu_limits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tarinfo = tarfile.TarInfo('123/' * 126 + 'longname')
    tarinfo.tobuf(tarfile.GNU_FORMAT)
    tarinfo = tarfile.TarInfo('longlink')
    tarinfo.linkname = '123/' * 126 + 'longname'
    tarinfo.tobuf(tarfile.GNU_FORMAT)
    tarinfo = tarfile.TarInfo('name')
    tarinfo.uid = 72057594037927936
    self.assertRaises(ValueError, tarinfo.tobuf, tarfile.GNU_FORMAT)
