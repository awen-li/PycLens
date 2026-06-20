# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LongnameTest_test_read_longlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    longname = self.subdir + '/' + '123/' * 125 + 'longname'
    longlink = self.subdir + '/' + '123/' * 125 + 'longlink'
    try:
        tarinfo = self.tar.getmember(longlink)
    except KeyError:
        self.fail('longlink not found')
    self.assertEqual(tarinfo.linkname, longname, 'linkname wrong')
