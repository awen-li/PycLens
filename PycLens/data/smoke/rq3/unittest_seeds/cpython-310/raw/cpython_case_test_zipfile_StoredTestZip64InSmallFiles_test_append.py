# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: StoredTestZip64InSmallFiles_test_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with zipfile.ZipFile(TESTFN2, 'w', allowZip64=True) as zipfp:
        zipfp.writestr('strfile', self.data)
    with zipfile.ZipFile(TESTFN2, 'r', allowZip64=True) as zipfp:
        zinfo = zipfp.getinfo('strfile')
        extra = zinfo.extra
    with zipfile.ZipFile(TESTFN2, 'a', allowZip64=True) as zipfp:
        zipfp.writestr('strfile2', self.data)
    with zipfile.ZipFile(TESTFN2, 'r', allowZip64=True) as zipfp:
        zinfo = zipfp.getinfo('strfile')
        self.assertEqual(zinfo.extra, extra)
