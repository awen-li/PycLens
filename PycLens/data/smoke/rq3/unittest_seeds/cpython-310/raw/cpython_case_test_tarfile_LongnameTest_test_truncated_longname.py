# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: LongnameTest_test_truncated_longname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    longname = self.subdir + '/' + '123/' * 125 + 'longname'
    tarinfo = self.tar.getmember(longname)
    offset = tarinfo.offset
    self.tar.fileobj.seek(offset)
    fobj = io.BytesIO(self.tar.fileobj.read(3 * 512))
    with self.assertRaises(tarfile.ReadError):
        tarfile.open(name='foo.tar', fileobj=fobj)
