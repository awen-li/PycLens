# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: UnicodeTest_test_unicode_filename_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tar = tarfile.open(tmpname, 'w', format=self.format, encoding='ascii', errors='strict')
    try:
        tarinfo = tarfile.TarInfo()
        tarinfo.name = 'äöü'
        self.assertRaises(UnicodeError, tar.addfile, tarinfo)
        tarinfo.name = 'foo'
        tarinfo.uname = 'äöü'
        self.assertRaises(UnicodeError, tar.addfile, tarinfo)
    finally:
        tar.close()
