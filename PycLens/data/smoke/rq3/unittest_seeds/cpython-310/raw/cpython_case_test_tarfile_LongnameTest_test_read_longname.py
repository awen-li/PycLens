# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LongnameTest_test_read_longname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    longname = self.subdir + '/' + '123/' * 125 + 'longname'
    try:
        tarinfo = self.tar.getmember(longname)
    except KeyError:
        self.fail('longname not found')
    self.assertNotEqual(tarinfo.type, tarfile.DIRTYPE, 'read longname as dirtype')
