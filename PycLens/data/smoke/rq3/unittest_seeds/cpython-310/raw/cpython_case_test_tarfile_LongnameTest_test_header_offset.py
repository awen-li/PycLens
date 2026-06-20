# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LongnameTest_test_header_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    longname = self.subdir + '/' + '123/' * 125 + 'longname'
    offset = self.tar.getmember(longname).offset
    with open(tarname, 'rb') as fobj:
        fobj.seek(offset)
        tarinfo = tarfile.TarInfo.frombuf(fobj.read(512), 'iso8859-1', 'strict')
        self.assertEqual(tarinfo.type, self.longnametype)
